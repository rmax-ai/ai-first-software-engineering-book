# Execution

## Commands/tools run
- `view DEVELOPMENT.md`
- `view state/feature_iterations/iter_022/06-next-iteration.md`
- `apply_patch` on `state/copilot_sdk_smoke_test.py` to add `usage-examples-order-guard` mode.
- `uv run python state/copilot_sdk_smoke_test.py --mode stub`
- `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-order-guard`

## Files changed
- `state/copilot_sdk_smoke_test.py`
  - Added `run_usage_examples_order_guard_mode()` to assert generated non-`stub` usage command lines match registration order.
  - Registered `usage-examples-order-guard` in `TRACE_SUMMARY_MODE_SPECS`.
- `state/feature_iterations/iter_023/*.md`
  - Added iteration task, plan, validation, risks/decisions, next iteration, and summary artifacts.

## Rationale per change
- The new deterministic guard makes ordering regressions explicit and independent from duplicate coverage.
- Keeping the mode in metadata preserves existing parser/help/doc generation and dispatch wiring.
