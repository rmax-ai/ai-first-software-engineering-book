# Validation

## Verification commands run
- `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-coverage-guard`
- `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-order-guard`
- `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-mode-set-coverage-guard`

## Observed outputs/results
- `PASS: usage-examples-coverage-guard mode validates generated usage examples for non-stub modes`
- `PASS: usage-examples-order-guard mode validates generated usage examples preserve registration order`
- `PASS: usage-examples-mode-set-coverage-guard mode validates generated usage examples cover all non-stub modes exactly once`

## Pass/fail against acceptance criteria
- ✅ Shared expected non-`stub` mode helper added.
- ✅ Three targeted guard modes now reuse the helper.
- ✅ All required validation commands passed.
