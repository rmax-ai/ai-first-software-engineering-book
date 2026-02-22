# Next Iteration Recommendation

## Next task
Implement deterministic trace-summary diagnostics in `state/kernel.py` and expose the signals required for smoke/eval checks.

## Why this is next
Trace diagnostics are foundational for validating later role-IO and eval-contract updates; they provide the observability baseline needed by follow-up tests.

## Acceptance criteria
- Add structured trace-summary output for each kernel loop stage.
- Record deterministic metrics fields consumed by eval gates.
- Add/adjust targeted smoke coverage in `state/copilot_sdk_uv_smoke.py` for new trace signals.
- Update validation notes with executed `uv run python ...` commands and observed pass/fail evidence.

## Expected files to touch
- `state/kernel.py`
- `state/copilot_sdk_uv_smoke.py`
- `state/metrics.json`
