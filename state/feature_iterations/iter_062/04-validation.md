# Validation

## Verification commands run
- `uv run python state/copilot_sdk_uv_smoke.py --mode trace-summary --run-kernel-for-trace-summary`
- `uv run python state/copilot_sdk_uv_smoke.py --mode trace-summary-malformed-phase --run-kernel-for-trace-summary`
- `uv run python state/copilot_sdk_uv_smoke.py --mode trace-summary-malformed-phase-payload --run-kernel-for-trace-summary`
- `uv run python state/copilot_sdk_uv_smoke.py --mode trace-summary-missing-phase --run-kernel-for-trace-summary`

## Observed outputs/results
- `trace-summary`: **PASS** — `trace_summary present with required keys` and `phase_trace_events=3`.
- `trace-summary-malformed-phase`: **PASS** — expected failure observed: `phase_trace missing keys: ['budget_signal']`.
- `trace-summary-malformed-phase-payload`: **PASS** — expected failure observed: `phase_trace payload is not an object`.
- `trace-summary-missing-phase`: **PASS** — expected failure observed: `missing required phase traces: ['evaluation']`.

## Pass/fail against acceptance criteria
- AC1 (fixture-backed eligible kernel-run support without repository ledger mutation): **PASS**
- AC2 (all four kernel-run modes with expected outcomes): **PASS**
- AC3 (record command outputs and outcomes): **PASS**
