# Validation

## Verification commands run
- `uv run python state/copilot_sdk_uv_smoke.py --mode trace-summary`
- `uv run python state/copilot_sdk_uv_smoke.py --mode trace-summary-malformed-phase`
- `uv run python state/copilot_sdk_uv_smoke.py --mode trace-summary-malformed-phase-payload`

## Observed outputs/results
- `trace-summary`: `PASS: trace_summary present with required keys` and `phase_trace_events=3`.
- `trace-summary-malformed-phase`: `PASS: expected phase_trace validation failure observed: phase_trace missing keys: ['budget_signal']`.
- `trace-summary-malformed-phase-payload`: `PASS: expected phase_trace validation failure observed: phase_trace payload is not an object`.

## Pass/fail against acceptance criteria
- AC1 (non-object payload failure path): **PASS**
- AC2 (existing modes stay green): **PASS**
- AC3 (captured evidence): **PASS**
