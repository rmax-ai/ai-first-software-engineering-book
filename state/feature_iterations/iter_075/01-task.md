# Task

## Selected task title
Extract a shared parity cleanup target-mode helper and migrate parity guard modes to use it.

## Why this task now
The previous iteration identified repeated parity target tuples in multiple guard modes; extracting a single helper reduces drift risk with no behavior change.

## Acceptance criteria
1. Add one helper in `state/copilot_sdk_smoke_test.py` that returns the parity cleanup target-mode tuple.
2. Update all parity cleanup guard modes in `state/copilot_sdk_smoke_test.py` to use the helper without changing assertion intent.
3. Run `uv run python state/copilot_sdk_smoke_test.py --mode trace-summary-fixture-cleanup-parity-mode-choices-usage-examples-uniqueness-adjacency-guard` and `uv run python state/copilot_sdk_smoke_test.py --mode mode-choices-coverage-guard`, and record results.
