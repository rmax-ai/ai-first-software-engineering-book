# Next iteration

## Recommended next task
Add a deterministic guard mode that verifies `usage-examples-duplicate-count-mode-coverage-guard` itself remains included in argparse `--mode` choices and generated usage examples.

## Why it is next
The newest guard protects an important regression mode; a follow-on guard will keep this additional protection from silently dropping out of shared mode metadata.

## Concrete acceptance criteria
1. Add one deterministic guard in `state/copilot_sdk_smoke_test.py` that asserts `usage-examples-duplicate-count-mode-coverage-guard` is present in parser choices and generated usage lines.
2. Validate with:
   - `uv run python state/copilot_sdk_smoke_test.py --mode mode-choices-coverage-guard`
   - `uv run python state/copilot_sdk_smoke_test.py --mode <new-guard-mode>`

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_031/*.md`
