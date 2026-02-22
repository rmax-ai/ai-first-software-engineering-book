# Task: Add usage example coverage guard

## Why this task now
- Iteration 020 recommended guarding generated usage examples as the next deterministic documentation check.
- This is the smallest unfinished task in the current backlog and is isolated to smoke-test metadata integrity.

## Acceptance criteria
1. Add a deterministic smoke mode in `state/copilot_sdk_smoke_test.py` validating `_usage_doc_lines(...)` includes every non-`stub` mode exactly once.
2. Keep parser/dispatch behavior unchanged.
3. Validate with:
   - `uv run python state/copilot_sdk_smoke_test.py --mode stub`
   - `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-coverage-guard`
