# Execution

## Commands/tools run
1. `view state/llm_client.py`
2. `apply_patch` on `state/llm_client.py`
3. `uv run python state/copilot_sdk_smoke_test.py --mode stub`
4. `uv run python state/copilot_sdk_smoke_test.py --mode sdk-unavailable`
5. `uv run python - <<'PY' ... asyncio.run(main()) ... PY` (nested-loop bridge check)

## Files changed
- `state/llm_client.py`

## Short rationale per change
- Replaced ad-hoc event loop creation in running-loop contexts with a dedicated background SDK loop and `run_coroutine_threadsafe` bridge.
- Added loop/thread lifecycle cleanup in `_close_sdk_loop`.
- Added `_run_async` docstring documenting lifecycle behavior.
