# Task

## Selected task title
Add deterministic set/count coverage for generated non-`stub` usage modes.

## Why this task now
- `iter_023/06-next-iteration.md` prioritized completing the usage guard triplet after duplicate and order guards.
- Explicit set/count coverage catches missing or extra modes independent of ordering assertions.

## Acceptance criteria
1. Add one smoke mode in `state/copilot_sdk_smoke_test.py` that compares extracted non-`stub` usage mode names to non-`stub` `_all_mode_specs()` names as exact set and count match.
2. Keep parser/help/dispatch behavior unchanged.
3. Validate with:
   - `uv run python state/copilot_sdk_smoke_test.py --mode stub`
   - `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-mode-set-coverage-guard`
