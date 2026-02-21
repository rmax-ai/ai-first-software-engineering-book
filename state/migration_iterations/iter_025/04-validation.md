# Validation

## Verification commands
1. `python state/copilot_sdk_smoke_test.py --mode stub`
2. `python state/copilot_sdk_smoke_test.py --mode fallback-non-object`

## Observed results
- Command 1 output: `PASS: stub Copilot SDK path works`.
- Command 2 output: `PASS: deterministic HTTP fallback non-object payload mapping works`.
- Both commands exited with code `0`.

## Acceptance criteria status
- New non-object fallback mode added: **PASS**
- Error mapping assertion includes `HTTP fallback returned non-object payload`: **PASS**
- Mode fails on regression via assertion path: **PASS**

