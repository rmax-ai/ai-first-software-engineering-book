# Recommended next task

## Task

Persist kernel tracepoint aggregates into `state/metrics.json` per chapter iteration.

## Why it is next

Trace events now exist; the next smallest step is exposing summarized telemetry in the existing metrics structure for regression tracking.

## Acceptance criteria

1. Kernel writes a compact trace summary per iteration into `metrics.json` history entries.
2. Summary includes at least decision, drift score, diff ratio, and deterministic pass/fail.
3. Existing metrics consumers continue to parse without schema breakage.

## Expected files to touch

- `state/kernel.py`
- `state/metrics.json`
- Optional: `state/copilot_sdk_uv_smoke.py` (if smoke assertions are added)
