# Validation

## Verification commands run
1. `uv run python state/copilot_sdk_uv_smoke.py --mode trace-summary`
2. `uv run python state/copilot_sdk_uv_smoke.py --mode trace-summary-malformed-phase`

## Observed outputs/results
- `--mode trace-summary`:
  - `PASS: trace_summary present with required keys`
  - `trace_summary={'decision': 'accept', 'drift_score': 0.0, 'diff_ratio': 0.0, 'deterministic_pass': True}`
  - `phase_trace_events=3`
- `--mode trace-summary-malformed-phase`:
  - `PASS: expected phase_trace validation failure observed: phase_trace missing keys: ['budget_signal']`

## Acceptance criteria check
1. **Pass** — Added deterministic malformed `phase_trace` path and explicit expected-failure assertion mode.
2. **Pass** — Existing trace-summary success mode remains green.
3. **Pass** — Both success and malformed-path command outputs are captured in this file.
