# Task

## Selected task
Add a short alias smoke mode that asserts the newest long-form exact-once adjacency-order guard registration appears exactly once.

## Why this task now
- `state/feature_iterations/iter_148/06-next-iteration.md` prioritized exact-once coverage for the newest long-form mode after the adjacency-order pair check.
- A short alias mode makes the latest long-form guard easier to run from the published iteration index.

## Acceptance criteria
1. Add one smoke runner that asserts the newest long-form exact-once adjacency-order guard mode appears exactly once.
2. Register one `TRACE_SUMMARY_MODE_SPECS` entry for that alias runner.
3. Run `python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-wrapper-helper-newest-long-form-adjacency-order-guard-exact-once-adjacency-order-guard-exact-once` and capture PASS output.
