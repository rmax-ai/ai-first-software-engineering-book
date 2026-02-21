# Validation

## Verification commands run
1. `python -m py_compile state/copilot_sdk_smoke_test.py state/llm_client.py`
2. `uv run python state/copilot_sdk_smoke_test.py --mode fallback-timeout`

## Observed outputs/results
- Command 1: pass.
- Command 2: `PASS: deterministic HTTP fallback timeout mapping works`.

## Pass/fail against acceptance criteria
- New deterministic timeout mode exists and executes: PASS.
- Error assertion checks for `HTTP fallback timed out`: PASS.
- Regression causes assertion failure/non-zero exit: PASS.
