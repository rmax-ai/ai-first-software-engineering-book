# Next Iteration

## Recommended next task
Refactor duplicated deterministic shutdown-mode setup logic in `state/copilot_sdk_smoke_test.py` into a shared helper.

## Why it is next
The shutdown modes now cover key branches but repeat setup/teardown code, increasing maintenance risk for future reliability scenarios.

## Concrete acceptance criteria
- Add one helper to initialize/teardown a copilot test client for shutdown-mode tests.
- Reuse the helper in `shutdown-failure`, `stop-unavailable`, `destroy-failure`, and `force-stop-unavailable`.
- Preserve current mode behaviors and PASS outputs.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
