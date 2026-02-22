# Next iteration

## Recommended next task
Extract a shared helper for locating argparse `--mode` action and migrate parity guard modes to use it.

## Why it is next
Parity guard functions still duplicate parser action lookup boilerplate; centralizing it will reduce noise and future drift.

## Concrete acceptance criteria
1. Add one helper in `state/copilot_sdk_smoke_test.py` that returns the argparse `--mode` action for a parser.
2. Update parity cleanup guard modes to use that helper without changing current assertions.
3. Run `uv run python state/copilot_sdk_smoke_test.py --mode trace-summary-fixture-cleanup-parity-mode-choices-usage-examples-adjacency-guard` and `uv run python state/copilot_sdk_smoke_test.py --mode mode-choices-coverage-guard`, and record results in `state/feature_iterations/iter_076/04-validation.md`.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_076/*.md`
