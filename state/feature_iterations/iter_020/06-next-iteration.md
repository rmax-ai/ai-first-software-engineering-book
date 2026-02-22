# Next Iteration

## Recommended next task
Add deterministic coverage that generated usage examples include every non-default mode exactly once.

## Why it is next
After guarding module docs, mode help text, and parser choices, usage example drift remains the next user-facing documentation vector.

## Concrete acceptance criteria
1. Add one deterministic smoke mode in `state/copilot_sdk_smoke_test.py` that validates `_usage_doc_lines(...)` includes one command for every registered non-`stub` mode.
2. Keep parser dispatch behavior unchanged.
3. Validate with:
   - `uv run python state/copilot_sdk_smoke_test.py --mode stub`
   - `uv run python state/copilot_sdk_smoke_test.py --mode <new-usage-coverage-guard-mode>`

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_021/*.md`
