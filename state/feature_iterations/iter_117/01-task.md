# Task

## Selected task title
Add adjacency smoke guard for uniqueness-adjacency-uniqueness mode ordering.

## Why this task now
`iter_116/06-next-iteration.md` recommends protecting ordering drift by asserting `...-uniqueness-guard` stays immediately before `usage-examples-mode-set-coverage-guard`.

## Acceptance criteria
1. Add one new smoke mode in `state/copilot_sdk_smoke_test.py` that asserts `...-uniqueness-guard` is adjacent to `usage-examples-mode-set-coverage-guard`.
2. Register the new mode in `TRACE_SUMMARY_MODE_SPECS` with deterministic description text.
3. Run `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-guard` and record PASS output.
