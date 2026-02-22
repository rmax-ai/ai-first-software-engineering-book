# Task: Share expected usage mode-name helper

## Why this task now
`iter_025/06-next-iteration.md` called out duplicated expected non-`stub` mode-name comprehensions across usage-example guards, which risks drift.

## Acceptance criteria
1. Add one private helper in `state/copilot_sdk_smoke_test.py` to compute expected non-`stub` mode names from mode specs.
2. Update `usage-examples-coverage-guard`, `usage-examples-order-guard`, and `usage-examples-mode-set-coverage-guard` to reuse the helper.
3. Validate with:
   - `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-coverage-guard`
   - `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-order-guard`
   - `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-mode-set-coverage-guard`
