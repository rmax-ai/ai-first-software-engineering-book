# Validation

## Verification commands run
1. `python -m py_compile state/llm_client.py state/copilot_sdk_smoke_test.py`
2. `uv run python state/copilot_sdk_smoke_test.py --mode fallback-connection-error`
3. `uv run python state/copilot_sdk_smoke_test.py --mode fallback`
4. `uv run python state/copilot_sdk_smoke_test.py --mode fallback-error`
5. `uv run python state/copilot_sdk_smoke_test.py --mode fallback-invalid-json`

## Observed outputs/results
- Command 1: pass.
- Command 2: `PASS: deterministic HTTP fallback connection error mapping works`.
- Command 3: `PASS: deterministic HTTP fallback path works`.
- Command 4: `PASS: deterministic HTTP fallback error mapping works`.
- Command 5: `PASS: deterministic HTTP fallback invalid JSON mapping works`.

## Pass/fail against acceptance criteria
- Fallback transport failure forced without external dependencies: PASS.
- Error message includes `HTTP fallback connection failed`: PASS.
- Mode fails on regression via assertion/non-zero exit: PASS.
