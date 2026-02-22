# Validation

## Verification commands run
1. `uv run python state/copilot_sdk_smoke_test.py --mode stub`
2. `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-order-guard`

## Observed outputs/results
- Command 1: `PASS: stub Copilot SDK path works`
- Command 2: `PASS: usage-examples-order-guard mode validates generated usage examples preserve registration order`

## Pass/fail against acceptance criteria
1. **Pass** — Added `usage-examples-order-guard` mode asserting non-`stub` usage lines preserve metadata registration order.
2. **Pass** — Parser/dispatch stay metadata-driven through existing `_all_mode_specs()` flow.
3. **Pass** — Both targeted smoke commands executed successfully.
