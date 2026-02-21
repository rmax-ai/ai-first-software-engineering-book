# Validation

## Verification commands run
- `uv run python state/copilot_sdk_smoke_test.py --mode stub`
- `uv run python state/copilot_sdk_smoke_test.py --mode sdk-unavailable`

## Observed outputs/results
- `PASS: stub Copilot SDK path works`
- `PASS: copilot provider requires SDK when module is unavailable`

## Pass/fail against acceptance criteria
- Bounded wait added in `_ensure_sdk_thread_loop`: **PASS**
- Bootstrap stage failures mapped to `LLMClientError`: **PASS**
- Required smoke checks passing: **PASS**
