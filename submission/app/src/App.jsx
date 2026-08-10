import React, { useEffect, useState } from "react";

const FIXTURES = Array.from({ length: 15 }, (_, i) => `PUB-${String(i + 1).padStart(2, "0")}`);

export default function App() {
  const [view, setView] = useState("review");
  const [fixtureId, setFixtureId] = useState("PUB-01");
  const [packet, setPacket] = useState(null);
  const [ontology, setOntology] = useState(null);
  const [graph, setGraph] = useState(null);
  const [error, setError] = useState("");
  const [stopped, setStopped] = useState(false);

  async function runReview() {
    if (stopped) {
      setError("Emergency stop active — clear stop to continue advisory runs.");
      return;
    }
    setError("");
    try {
      const res = await fetch(`/v1/workflows/run/${fixtureId}`, { method: "POST" });
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      setPacket(await res.json());
    } catch (e) {
      setError(String(e.message || e));
    }
  }

  async function loadOntologyGraph() {
    setError("");
    try {
      const [o, g] = await Promise.all([
        fetch("/v1/ontology").then((r) => r.json()),
        fetch("/v1/graph?workflow=batch").then((r) => r.json()),
      ]);
      setOntology(o);
      setGraph(g);
    } catch (e) {
      setError(String(e.message || e));
      setGraph({ mode: "unavailable", advisory: true, nodes: [], edges: [] });
    }
  }

  useEffect(() => {
    if (view === "ontology") loadOntologyGraph();
  }, [view]);

  return (
    <>
      <header>
        <h1>AEGIS Evidence Review</h1>
        <p>
          Advisory only — this UI cannot release, reject, allocate, ship, recall, or finalize PV
          decisions. Humans remain accountable (transparency Art.13/50).
        </p>
      </header>
      <div className="banner" role="status">
        Outputs are decision-support packets. Regulated actions require authorized human systems
        outside AEGIS. Graph/ontology views are derived and may be incomplete.
      </div>
      <main>
        <nav aria-label="Primary">
          <button className={view === "review" ? "active" : ""} onClick={() => setView("review")}>
            Workflow review
          </button>
          <button
            className={view === "ontology" ? "active" : ""}
            onClick={() => setView("ontology")}
          >
            Ontology / KG dashboard
          </button>
          <button
            className={stopped ? "active" : ""}
            onClick={() => setStopped((s) => !s)}
            aria-pressed={stopped}
          >
            {stopped ? "Emergency stop ON (click to clear)" : "Emergency stop"}
          </button>
          <p className="sr-only">
            No controls exist for batch disposition, PV finals, allocation, shipment, or recall.
          </p>
        </nav>
        <section className="panel" aria-live="polite">
          {error && (
            <p className="tag danger" role="alert">
              {error}
            </p>
          )}
          {view === "review" && (
            <>
              <label htmlFor="fixture">Public fixture</label>
              <select
                id="fixture"
                value={fixtureId}
                onChange={(e) => setFixtureId(e.target.value)}
                style={{ display: "block", width: "100%", margin: "0.5rem 0 1rem" }}
              >
                {FIXTURES.map((f) => (
                  <option key={f} value={f}>
                    {f}
                  </option>
                ))}
              </select>
              <button onClick={runReview}>Assemble advisory packet</button>
              {packet && (
                <div style={{ marginTop: "1rem" }}>
                  <span className="tag">execution: {packet.execution_status}</span>
                  {packet.readiness_state && (
                    <span className="tag warn">readiness: {packet.readiness_state}</span>
                  )}
                  <span className="tag">
                    human review: {packet.human_review?.role || "required"}
                  </span>
                  <h2>Contradictions / gaps / abstentions</h2>
                  <pre>
                    {JSON.stringify(
                      {
                        contradictions: packet.contradictions,
                        gaps: packet.gaps,
                        abstentions: packet.abstentions,
                        blocked_actions: packet.blocked_actions,
                      },
                      null,
                      2
                    )}
                  </pre>
                  <h2>Full packet (export)</h2>
                  <pre>{JSON.stringify(packet, null, 2)}</pre>
                </div>
              )}
            </>
          )}
          {view === "ontology" && (
            <>
              <h2>Ontology</h2>
              <pre>{JSON.stringify(ontology, null, 2)}</pre>
              <h2>Knowledge graph (advisory)</h2>
              <p className="tag warn">
                mode: {graph?.mode || "unknown"} — not system of record
              </p>
              <pre>{JSON.stringify(graph, null, 2)}</pre>
            </>
          )}
        </section>
      </main>
    </>
  );
}
