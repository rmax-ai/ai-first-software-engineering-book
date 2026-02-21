# Validation

## Verification commands run
1. `python -m py_compile state/llm_client.py state/copilot_sdk_smoke_test.py`
2. `python state/copilot_sdk_smoke_test.py --mode stub`
3. `python state/copilot_sdk_smoke_test.py --mode fallback`

## Observed outputs/results
- Command 1: pass.
- Command 2: `PASS: stub Copilot SDK path works` with expected token usage output.
- Command 3: `PASS: deterministic HTTP fallback path works` with expected token usage output.

## Acceptance criteria status
- Deterministic fallback mode added: PASS
- Content + usage extraction assertions added: PASS
- Non-zero failure behavior on regression (assertions): PASS
