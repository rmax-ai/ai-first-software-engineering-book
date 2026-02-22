# Next Iteration

## Recommended next task
Add deterministic coverage that argparse `--mode` choices remain exactly aligned with registered mode metadata.

## Why it is next
After guarding module docs and mode-help descriptions, the remaining parser-facing drift vector is the `choices` list itself.

## Concrete acceptance criteria
1. Add one deterministic smoke mode in `state/copilot_sdk_smoke_test.py` that validates parser `--mode` choices contain every registered mode name exactly once.
2. Keep existing mode dispatch behavior unchanged.
3. Validate with:
   - `uv run python state/copilot_sdk_smoke_test.py --mode stub`
   - `uv run python state/copilot_sdk_smoke_test.py --mode <new-choices-guard-mode>`

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_020/*.md`
