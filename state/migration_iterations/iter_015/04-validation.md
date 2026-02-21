# Validation

## Verification commands run
1. `uv run python state/copilot_sdk_smoke_test.py --mode stub`
2. `uv run python state/copilot_sdk_uv_smoke.py --mode ping --model gpt-5 --timeout 30`
3. Static diagnostics:
   - `get_errors` for `state/llm_client.py` and `state/kernel.py`

## Observed outputs/results
- Stub smoke: **PASS** (`content='stub-ok: ping'`, usage prompt/completion = `7/3`).
- SDK ping smoke: **PASS** (`pong: health check`).
- `state/kernel.py`: no diagnostics.
- `state/llm_client.py`: existing broad typing diagnostics remain (dynamic SDK API `Any`/awaitability patterns), but runtime smoke checks succeeded.

## Pass/fail against acceptance criteria
- Usage extraction and event normalization hardening: **PASS**
- Bounded kernel cleanup behavior: **PASS**
- Focused smoke checks passing: **PASS**
