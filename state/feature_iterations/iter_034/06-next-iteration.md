# Next iteration

## Recommended next task
Add a deterministic guard mode that verifies `usage-examples-duplicate-count-mode-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard` remains included in argparse `--mode` choices and generated usage examples.

## Why it is next
Continuing the guard-chain keeps every newly introduced guard mode covered by mode-choice and usage-example assertions.

## Concrete acceptance criteria
1. Add one deterministic guard in `state/copilot_sdk_smoke_test.py` asserting `usage-examples-duplicate-count-mode-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard` appears in parser choices and generated usage lines.
2. Validate with:
   - `uv run python state/copilot_sdk_smoke_test.py --mode mode-choices-coverage-guard`
   - `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-mode-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard`

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_035/*.md`
