# Next Iteration

## Recommended next task
Add deterministic coverage that module usage examples include every non-`stub` mode from `_all_mode_specs()` exactly once after order and duplicate guards.

## Why it is next
- Order and duplicate checks now exist independently; explicit one-to-one mode-to-usage coverage will complete the generated usage guard triplet.

## Concrete acceptance criteria
1. Add one smoke mode in `state/copilot_sdk_smoke_test.py` that compares extracted non-`stub` mode names from generated usage lines to non-`stub` `_all_mode_specs()` names as an exact set and count match.
2. Keep parser/help/dispatch behavior unchanged.
3. Validate with:
   - `uv run python state/copilot_sdk_smoke_test.py --mode stub`
   - `uv run python state/copilot_sdk_smoke_test.py --mode <new-usage-mode-set-coverage-guard-mode>`

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_024/*.md`
