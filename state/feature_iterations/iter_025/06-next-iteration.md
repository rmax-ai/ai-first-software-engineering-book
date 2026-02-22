# Next Iteration

## Recommended next task
Refactor usage-example guard modes to share a companion helper that computes expected non-`stub` mode names from `_all_mode_specs()` once.

## Why it is next
Current guard modes still repeat expected non-`stub` mode-name comprehension logic, so consolidating it will further reduce drift between coverage/order/set assertions.

## Concrete acceptance criteria
1. Add one private helper in `state/copilot_sdk_smoke_test.py` that returns expected non-`stub` mode names from mode specs.
2. Update `usage-examples-coverage-guard`, `usage-examples-order-guard`, and `usage-examples-mode-set-coverage-guard` to use the helper.
3. Validate with:
   - `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-coverage-guard`
   - `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-order-guard`
   - `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-mode-set-coverage-guard`

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_026/*.md`
