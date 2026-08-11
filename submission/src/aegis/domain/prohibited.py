from __future__ import annotations

PROHIBITED_ACTIONS = frozenset(
    {
        "release_batch",
        "reject_batch",
        "recall_batch",
        "relabel_batch",
        "reprocess_batch",
        "final_seriousness",
        "final_causality",
        "final_expectedness",
        "final_reportability",
        "confirm_signal",
        "allocate_stock",
        "reserve_capacity",
        "change_inventory_status",
        "ship_product",
        "initiate_recall",
    }
)


def is_prohibited(action: str) -> bool:
    return action.strip().lower() in PROHIBITED_ACTIONS
