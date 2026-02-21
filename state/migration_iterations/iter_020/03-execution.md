# Execution

## Commands/tools run
- `python -m py_compile state/llm_client.py state/copilot_sdk_smoke_test.py`
- `python state/copilot_sdk_smoke_test.py --mode stub`
- `python state/copilot_sdk_smoke_test.py --mode fallback`
- `python state/copilot_sdk_smoke_test.py --mode fallback-error`

## Files changed
- `state/copilot_sdk_smoke_test.py`

## Rationale
- Added a deterministic `fallback-error` mode to lock in HTTP fallback failure behavior.
- Reused local stdlib server + import monkeypatch pattern to keep test offline and deterministic.
- Added explicit assertion for HTTP status context in `LLMClientError` message.
