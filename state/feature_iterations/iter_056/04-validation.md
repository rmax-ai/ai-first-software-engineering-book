# Validation

## Verification commands run
1. `uv run python state/copilot_sdk_uv_smoke.py --mode trace-summary`

## Observed outputs/results
- Command exited successfully with:
  - `PASS: trace_summary present with required keys`
  - `trace_summary={'decision': 'accept', 'drift_score': 0.0, 'diff_ratio': 0.0, 'deterministic_pass': True}`
  - `phase_trace_events=3`

## Acceptance criteria check
1. **Pass** — Trace-summary mode now generates/reads deterministic synthetic metrics and trace data from the built-in fixture root.
2. **Pass** — Default trace-summary smoke invocation passed without pre-created repository fixture files.
3. **Pass** — Validation evidence is captured in this file.
