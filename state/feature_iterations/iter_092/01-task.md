# Task

## Selected task title
Add a deterministic smoke mode that fails if duplicate-count coverage-guard wrappers directly call `_all_mode_specs()`.

## Why this task now
`state/feature_iterations/iter_091/06-next-iteration.md` prioritized a regression guard to protect the newly centralized duplicate-count wrapper helper pattern.

## Acceptance criteria
1. Add one new mode in `state/copilot_sdk_smoke_test.py` that inspects duplicate-count wrapper source and fails on direct `_all_mode_specs()` usage.
2. Register the mode in the mode-spec table with a clear description.
3. Run `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-wrapper-all-mode-specs-guard` and record PASS output.
