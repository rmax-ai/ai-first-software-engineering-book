# Next Iteration

## Recommended next task
Add deterministic coverage that the generated usage block contains no duplicate mode command lines.

## Why it is next
- Current guard ensures expected inclusion, but an explicit duplicate-detection check hardens documentation integrity against accidental repeated entries.

## Concrete acceptance criteria
1. Add one smoke mode in `state/copilot_sdk_smoke_test.py` that asserts generated non-`stub` usage command lines are unique.
2. Keep parser/dispatch behavior unchanged.
3. Validate with:
   - `uv run python state/copilot_sdk_smoke_test.py --mode stub`
   - `uv run python state/copilot_sdk_smoke_test.py --mode <new-usage-duplicates-guard-mode>`

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_022/*.md`
