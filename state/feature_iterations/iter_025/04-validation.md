# Validation

## Verification commands run
- `uv run python state/copilot_sdk_smoke_test.py --mode stub`
- `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-order-guard`
- `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-mode-set-coverage-guard`

## Observed outputs/results
- `PASS: stub Copilot SDK path works`
- `PASS: usage-examples-order-guard mode validates generated usage examples preserve registration order`
- `PASS: usage-examples-mode-set-coverage-guard mode validates generated usage examples cover all non-stub modes exactly once`

## Acceptance criteria status
- ✅ Shared helper for generated non-`stub` usage mode extraction added.
- ✅ Usage-example guard modes now reuse helper without changing guard intent.
- ✅ All required validation commands passed.
