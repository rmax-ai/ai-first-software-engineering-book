# Next Iteration Recommendation

## Task
Implement the smallest observability slice in `state/kernel.py` by adding deterministic trace-summary logging for one additional kernel decision point.

## Why this is next
This converts the new planning backlog into a measurable code change with low risk and immediately improves harness visibility.

## Acceptance criteria
- Add a focused kernel trace output for one decision branch without changing public CLI behavior.
- Add/adjust targeted tests under `state/` that prove deterministic output shape.
- Run relevant harness verification (including a focused `uv run python state/copilot_sdk_uv_smoke.py` mode if applicable) and record evidence.

## Expected files to touch
- `state/kernel.py`
- Targeted test file(s) under `state/`
- `state/feature_iterations/iter_002/04-validation.md`
