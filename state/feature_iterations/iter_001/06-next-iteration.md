# Next Iteration Recommendation

## Recommended next task
Implement structured kernel trace summaries in `state/kernel.py` so each run emits deterministic per-phase metrics suitable for regression checks.

## Why this is next
- It is the highest-leverage feature item from the new backlog because it improves observability and strengthens downstream validation.
- It directly supports reliable interpretation of smoke/eval results before expanding role templates or test coverage.

## Acceptance criteria
- Add deterministic trace-summary generation in `state/kernel.py` with stable field names and ordering.
- Ensure trace output is consumed/validated by a targeted deterministic smoke mode in `state/copilot_sdk_uv_smoke.py`.
- Document expected signals and regression behavior in the corresponding iteration validation artifact.
- Run and record at least one targeted verification command using UV runtime.

## Expected files to touch
- `state/kernel.py`
- `state/copilot_sdk_uv_smoke.py`
- `state/feature_iterations/iter_002/04-validation.md`
