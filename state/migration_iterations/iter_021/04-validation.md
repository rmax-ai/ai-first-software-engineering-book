# Validation

## Verification commands run
1. `python -m py_compile state/llm_client.py state/copilot_sdk_smoke_test.py`
2. `python state/copilot_sdk_smoke_test.py --mode stub`
3. `python state/copilot_sdk_smoke_test.py --mode fallback`
4. `python state/copilot_sdk_smoke_test.py --mode fallback-invalid-json`

## Observed outputs/results
- Command 1: pass.
- Command 2: `PASS: stub Copilot SDK path works`.
- Command 3: `PASS: deterministic HTTP fallback path works`.
- Command 4: `PASS: deterministic HTTP fallback invalid JSON mapping works`.

## Acceptance criteria status
- Forced fallback non-JSON path executed: PASS
- Error includes `HTTP fallback returned invalid JSON` context: PASS
- Regression fails via assertions/non-zero exit: PASS
