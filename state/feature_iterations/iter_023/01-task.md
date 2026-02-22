# Task

## Selected task title
Add deterministic ordering coverage for generated non-`stub` usage command lines.

## Why this task now
- `iter_022/06-next-iteration.md` prioritized an explicit ordering guard after duplicate coverage was added.
- Ordering regressions can silently change generated usage docs even when all modes still exist.

## Acceptance criteria
1. Add one smoke mode in `state/copilot_sdk_smoke_test.py` that asserts generated non-`stub` usage lines preserve `_all_mode_specs()` registration order.
2. Keep parser and dispatch behavior unchanged.
3. Validate with:
   - `uv run python state/copilot_sdk_smoke_test.py --mode stub`
   - `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-order-guard`
