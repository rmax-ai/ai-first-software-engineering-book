# Task: Persist kernel trace summaries into metrics history

## Why this task now
`iter_002` recommended exposing tracepoint outcomes in `state/metrics.json` so telemetry is queryable by existing regression workflows.

## Acceptance criteria
- Add a compact per-iteration trace summary to `metrics.json` history entries.
- Summary includes decision, drift score, diff ratio, and deterministic pass/fail.
- Existing metrics structure remains backward compatible for current consumers.
