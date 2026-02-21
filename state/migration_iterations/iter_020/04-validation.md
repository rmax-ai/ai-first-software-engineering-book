# Validation

## Verification commands run
1. `python -m py_compile state/llm_client.py state/copilot_sdk_smoke_test.py`
2. `uv run python state/copilot_sdk_smoke_test.py --mode stub`
3. `uv run python state/copilot_sdk_smoke_test.py --mode fallback`
4. `uv run python state/copilot_sdk_smoke_test.py --mode fallback-error`

## Observed outputs/results
- Command 1: pass.
- Command 2: `PASS: stub Copilot SDK path works`.
- Command 3: `PASS: deterministic HTTP fallback path works`.
- Command 4: `PASS: deterministic HTTP fallback error mapping works`.

## Acceptance criteria status
- Forced fallback HTTP 500 path executed: PASS
- Error message contains HTTP status context: PASS
- Regression triggers non-zero failure through assertions: PASS
