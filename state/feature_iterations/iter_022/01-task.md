# Task: Add usage example duplicate-line guard

## Why this task now
- Iteration 021 identified duplicate detection as the next smallest hardening step for generated usage docs.
- This closes a remaining gap in deterministic checks for smoke-test module documentation output.

## Acceptance criteria
1. Add one deterministic smoke mode in `state/copilot_sdk_smoke_test.py` that asserts generated non-`stub` usage command lines are unique.
2. Keep parser/dispatch behavior unchanged.
3. Validate with:
   - `uv run python state/copilot_sdk_smoke_test.py --mode stub`
   - `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicates-guard`
