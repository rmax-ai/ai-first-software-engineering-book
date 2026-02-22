# Recommended next task

## Task
Table-drive shutdown-mode registration (`choices`, help text fragment, and dispatch) in `state/copilot_sdk_smoke_test.py`.

## Why it is next
- Shutdown modes still use repeated literal lists and branches, which now stand out as the next major drift hotspot.

## Acceptance criteria
1. Introduce one mapping for shutdown mode name, handler, and description.
2. Reuse the mapping in argparse choices/help and mode dispatch without changing behavior.
3. Re-run at least `stop-close-idempotency`, `stop-failure-destroy-failure-close-idempotency`, and `trace-summary`.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_015/*`
