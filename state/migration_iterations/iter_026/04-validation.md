# Validation

## Verification commands
1. `python state/copilot_sdk_smoke_test.py --mode stub`
2. `python state/copilot_sdk_smoke_test.py --mode sdk-unavailable`

## Observed results
- Command 1 output: `PASS: stub Copilot SDK path works`.
- Command 2 output: `PASS: copilot provider requires SDK when module is unavailable`.
- Both commands exited with code `0`.

## Acceptance criteria status
- Copilot provider no longer routes to HTTP fallback: **PASS**
- Missing SDK raises clear SDK-required `LLMClientError`: **PASS**
- Stub smoke mode remains green: **PASS**
