# Validation

## Verification commands run
1. `python -m py_compile state/llm_client.py state/copilot_sdk_smoke_test.py`
2. `python state/copilot_sdk_smoke_test.py --mode stub`
3. `python state/copilot_sdk_smoke_test.py --mode fallback`
4. `python state/copilot_sdk_smoke_test.py --mode fallback-error`
5. `python state/copilot_sdk_smoke_test.py --mode fallback-invalid-json`
6. `for i in $(seq 1 10); do python state/copilot_sdk_smoke_test.py --mode fallback-error >/dev/null; done`

## Observed outputs/results
- Command 1: pass.
- Command 2: `PASS: stub Copilot SDK path works`.
- Command 3: `PASS: deterministic HTTP fallback path works`.
- Command 4: `PASS: deterministic HTTP fallback error mapping works`.
- Command 5: `PASS: deterministic HTTP fallback invalid JSON mapping works`.
- Command 6: all 10 repeated runs passed.

## Pass/fail against acceptance criteria
- Repeated `fallback-error` reliability: PASS.
- Actionable HTTP status assertion preserved: PASS.
- Regression still fails via assertion/non-zero behavior when broken: PASS (assertion remains in mode implementation).
