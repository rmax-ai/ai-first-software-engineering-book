# Next Iteration

## Recommended next task
Add deterministic ordering coverage that generated non-`stub` usage command lines match metadata registration order.

## Why it is next
- Coverage and duplicate guards now exist; explicit order validation independently protects against accidental reordering regressions.

## Concrete acceptance criteria
1. Add one smoke mode in `state/copilot_sdk_smoke_test.py` asserting generated non-`stub` usage command lines appear in the same order as `_all_mode_specs()`.
2. Keep parser/dispatch behavior unchanged.
3. Validate with:
   - `uv run python state/copilot_sdk_smoke_test.py --mode stub`
   - `uv run python state/copilot_sdk_smoke_test.py --mode <new-usage-order-guard-mode>`

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_023/*.md`
