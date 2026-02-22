# Recommended next task

## Task
Refactor deterministic trace-summary smoke mode registration into a single table-driven mapping.

## Why it is next
- The mode list, help text, and dispatch branches are now repetitive and error-prone.
- A table-driven layout will reduce drift when adding future deterministic guards.

## Acceptance criteria
1. Introduce a single mapping source for trace-summary mode names, handlers, and descriptions.
2. Keep CLI behavior and existing mode outputs unchanged.
3. Re-run at least `trace-summary`, `trace-summary-missing-entry-guard`, and one shutdown mode to confirm no regressions.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_014/*`
