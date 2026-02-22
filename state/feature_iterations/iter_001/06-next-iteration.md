# Next iteration recommendation

## Recommended task
Implement deterministic trace-summary schema guards in `state/copilot_sdk_smoke_test.py` and wire them into the table-driven mode matrix.

## Why this is next
The seed plan depends on observable, regression-testable traces; adding smoke guards first provides immediate safety before editing kernel orchestration logic.

## Acceptance criteria
- Add one new deterministic smoke mode that validates trace-summary schema shape and required keys.
- Ensure the new mode is registered in the shared table-driven mode spec used for CLI choices/help and dispatch.
- Execute `uv run python state/copilot_sdk_smoke_test.py --mode <new-mode>` successfully and capture result in validation artifacts.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_002/03-execution.md`
- `state/feature_iterations/iter_002/04-validation.md`
