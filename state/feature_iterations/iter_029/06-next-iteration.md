# Next iteration

## Recommended next task
Add a deterministic guard mode that verifies the duplicate-count regression mode remains included in argparse `--mode` choices and generated usage examples after future mode-table edits.

## Why it is next
The new regression logic is table-driven; a focused coverage guard will prevent accidental metadata drift that could silently remove this mode from runnable surfaces.

## Concrete acceptance criteria
1. Add one deterministic guard in `state/copilot_sdk_smoke_test.py` that asserts `usage-examples-duplicate-count-regression-guard` is present in parser choices and generated usage lines.
2. Validate with:
   - `uv run python state/copilot_sdk_smoke_test.py --mode mode-choices-coverage-guard`
   - `uv run python state/copilot_sdk_smoke_test.py --mode <new-guard-mode>`

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_030/*.md`
