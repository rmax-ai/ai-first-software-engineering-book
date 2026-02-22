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
- AC1 (single mode-spec map across all four trace-summary modes): **PASS**
- AC2 (shared map reused in argparse choices and dispatch): **PASS**
- AC3 (all four trace-summary smoke modes re-run and recorded): **PASS**
