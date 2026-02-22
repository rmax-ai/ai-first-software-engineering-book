# Next iteration recommendation

## Exactly 1 recommended next task
Implement trace-summary guard instrumentation in `state/copilot_sdk_smoke_test.py` and `state/copilot_sdk_uv_smoke.py` to enforce parity between usage-example mode choices and fixture-cleanup trace-summary outputs.

## Why it is next
- It is the smallest high-impact slice from the new plan and improves deterministic observability without broad kernel refactoring.
- It creates immediate, testable signals that later kernel and eval updates can rely on.

## Acceptance criteria
- Add one new smoke-mode guard that fails when trace-summary mode choices drift from usage-example parity expectations.
- Ensure the guard is reachable via existing smoke execution paths and documented in test output.
- Execute `uv run python state/copilot_sdk_uv_smoke.py` and record pass/fail evidence in the next iteration `04-validation.md`.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
- `state/copilot_sdk_uv_smoke.py`
- `state/feature_iterations/iter_002/04-validation.md`
