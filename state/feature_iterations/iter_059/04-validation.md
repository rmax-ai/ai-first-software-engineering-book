# Validation

## Verification commands run
- `uv run python state/copilot_sdk_uv_smoke.py --mode trace-summary`
- `uv run python state/copilot_sdk_uv_smoke.py --mode trace-summary-malformed-phase`
- `uv run python state/copilot_sdk_uv_smoke.py --mode trace-summary-malformed-phase-payload`
- `uv run python state/copilot_sdk_uv_smoke.py --mode trace-summary-missing-phase`

## Observed outputs/results
- `trace-summary`: `PASS: trace_summary present with required keys` and `phase_trace_events=3`.
- `trace-summary-malformed-phase`: `PASS: expected phase_trace validation failure observed: phase_trace missing keys: ['budget_signal']`.
- `trace-summary-malformed-phase-payload`: `PASS: expected phase_trace validation failure observed: phase_trace payload is not an object`.
- `trace-summary-missing-phase`: `PASS: expected phase_trace validation failure observed: missing required phase traces: ['evaluation']`.

## Pass/fail against acceptance criteria
- AC1 (missing required phase failure path): **PASS**
- AC2 (existing modes remain green): **PASS**
- AC3 (validation evidence recorded): **PASS**
