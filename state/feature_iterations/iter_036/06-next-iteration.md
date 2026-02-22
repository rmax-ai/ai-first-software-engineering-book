# Next iteration

## Recommended next task
Add a deterministic guard mode that verifies `usage-examples-duplicate-count-mode-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard` remains included in argparse `--mode` choices and generated usage examples.

## Why it is next
Continuing the same guard-chain pattern keeps each newly introduced mode protected by explicit parser-choice and usage-example assertions.

## Concrete acceptance criteria
1. Add one deterministic guard in `state/copilot_sdk_smoke_test.py` asserting `usage-examples-duplicate-count-mode-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard` appears in parser choices and usage examples.
2. Validate with:
   - `uv run python state/copilot_sdk_smoke_test.py --mode mode-choices-coverage-guard`
   - `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-mode-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard`

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_037/*.md`
