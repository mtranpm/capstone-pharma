from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any, Sequence


@dataclass(frozen=True)
class AgreementReport:
    """Inter-rater agreement for advisory labels only — never a safety hard gate."""

    status: str
    cohen_kappa: float | None
    weighted_kappa: float | None
    gwet_ac1: float | None
    n_pairs: int
    soft_threshold: float
    notes: str

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def _cohen_kappa(a: Sequence[Any], b: Sequence[Any]) -> float:
    n = len(a)
    if n == 0:
        return 0.0
    labels = sorted(set(a) | set(b), key=str)
    # Observed agreement
    po = sum(1 for x, y in zip(a, b) if x == y) / n
    # Expected agreement
    pe = 0.0
    for lab in labels:
        pe += (sum(1 for x in a if x == lab) / n) * (sum(1 for y in b if y == lab) / n)
    if pe >= 1.0:
        return 1.0 if po >= 1.0 else 0.0
    return (po - pe) / (1.0 - pe)


def _gwet_ac1(a: Sequence[Any], b: Sequence[Any]) -> float:
    n = len(a)
    if n == 0:
        return 0.0
    labels = sorted(set(a) | set(b), key=str)
    q = max(len(labels), 1)
    po = sum(1 for x, y in zip(a, b) if x == y) / n
    # Gwet chance agreement
    pe = 0.0
    for lab in labels:
        pk = (sum(1 for x in a if x == lab) + sum(1 for y in b if y == lab)) / (2 * n)
        pe += pk * (1 - pk)
    pe = pe / max(q - 1, 1) if q > 1 else 0.0
    if pe >= 1.0:
        return 1.0 if po >= 1.0 else 0.0
    return (po - pe) / (1.0 - pe)


def _weighted_kappa_linear(a: Sequence[Any], b: Sequence[Any]) -> float | None:
    """Linear weighted κ for ordinal labels encoded as ints; None if non-ordinal."""
    try:
        ai = [int(x) for x in a]
        bi = [int(x) for x in b]
    except (TypeError, ValueError):
        return None
    labels = sorted(set(ai) | set(bi))
    if len(labels) < 2:
        return 1.0 if ai == bi else 0.0
    # Map to ranks
    index = {lab: i for i, lab in enumerate(labels)}
    k = len(labels)
    n = len(ai)
    weight = [[1.0 - abs(i - j) / (k - 1) for j in range(k)] for i in range(k)]
    obs = [[0.0] * k for _ in range(k)]
    for x, y in zip(ai, bi):
        obs[index[x]][index[y]] += 1.0 / n
    row = [sum(r) for r in obs]
    col = [sum(obs[i][j] for i in range(k)) for j in range(k)]
    po = sum(weight[i][j] * obs[i][j] for i in range(k) for j in range(k))
    pe = sum(weight[i][j] * row[i] * col[j] for i in range(k) for j in range(k))
    if pe >= 1.0:
        return 1.0 if po >= 1.0 else 0.0
    return (po - pe) / (1.0 - pe)


def compute_agreement(
    human_labels: Sequence[Any] | None,
    system_labels: Sequence[Any] | None,
    *,
    soft_threshold: float = 0.6,
) -> AgreementReport:
    """
    Compute Cohen κ / weighted κ / Gwet AC1 when paired labels exist.

    If labels are missing, returns status=pending_human_calibration with κ=None.
    Never fabricates agreement scores.
    """
    if not human_labels or not system_labels:
        return AgreementReport(
            status="pending_human_calibration",
            cohen_kappa=None,
            weighted_kappa=None,
            gwet_ac1=None,
            n_pairs=0,
            soft_threshold=soft_threshold,
            notes=(
                "No dual-annotated advisory label slice available. "
                "Do not invent κ. Soft threshold κ≥0.6 applies only after human calibration."
            ),
        )
    if len(human_labels) != len(system_labels):
        return AgreementReport(
            status="invalid_input",
            cohen_kappa=None,
            weighted_kappa=None,
            gwet_ac1=None,
            n_pairs=0,
            soft_threshold=soft_threshold,
            notes="human_labels and system_labels length mismatch",
        )

    cohen = _cohen_kappa(human_labels, system_labels)
    weighted = _weighted_kappa_linear(human_labels, system_labels)
    ac1 = _gwet_ac1(human_labels, system_labels)
    return AgreementReport(
        status="computed",
        cohen_kappa=cohen,
        weighted_kappa=weighted,
        gwet_ac1=ac1,
        n_pairs=len(human_labels),
        soft_threshold=soft_threshold,
        notes="Advisory fields only; not a safety hard gate",
    )
