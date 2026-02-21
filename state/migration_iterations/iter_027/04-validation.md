# Validation

## Verification commands run
1. `uv run python state/copilot_sdk_smoke_test.py --mode stub`
2. `uv run python state/copilot_sdk_smoke_test.py --mode sdk-unavailable`

## Observed outputs/results
- Stub mode: PASS (`stub-ok: ping`, usage prompt=7 completion=3).
- SDK-unavailable mode: PASS (error mapping assertion succeeded).

## Pass/fail against acceptance criteria
- Fallback method removed from `state/llm_client.py`: **PASS**.
- Fallback smoke helper functions removed: **PASS**.
- Required smoke modes pass: **PASS**.
