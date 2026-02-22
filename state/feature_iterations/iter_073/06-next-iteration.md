# Next iteration

## Recommended next task
Add a deterministic guard mode that enforces first-occurrence uniqueness before checking parity cleanup adjacency in both argparse choices and generated usage examples.

## Why it is next
This hardens the new adjacency check against duplicate-name regressions and makes parity-mode invariants explicit in a single focused assertion.

## Concrete acceptance criteria
1. Add one smoke mode in `state/copilot_sdk_smoke_test.py` that asserts each parity cleanup mode name appears exactly once and then verifies adjacency using those unique occurrences.
2. Run the new mode plus `mode-choices-coverage-guard` and `docstring-mode-coverage-guard`.
3. Record command outputs and pass/fail evidence in `state/feature_iterations/iter_074/04-validation.md`.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_074/*.md`
