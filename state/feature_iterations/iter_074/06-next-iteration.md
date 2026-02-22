# Next iteration

## Recommended next task
Extract a shared parity cleanup target-mode helper and migrate parity guard modes to use it.

## Why it is next
Multiple parity guard modes now repeat the same target tuple; a single helper will reduce drift risk while preserving deterministic checks.

## Concrete acceptance criteria
1. Add one helper in `state/copilot_sdk_smoke_test.py` that returns the parity cleanup target-mode tuple.
2. Update all parity cleanup guard modes in `state/copilot_sdk_smoke_test.py` to use the helper without changing current assertion intent.
3. Run `uv run python state/copilot_sdk_smoke_test.py --mode trace-summary-fixture-cleanup-parity-mode-choices-usage-examples-uniqueness-adjacency-guard` and `--mode mode-choices-coverage-guard`, then record results in `state/feature_iterations/iter_075/04-validation.md`.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_075/*.md`
