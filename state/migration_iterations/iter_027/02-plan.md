# Plan

1. Remove dead fallback method and imports from `state/llm_client.py`.
2. Remove dead fallback smoke helper functions/imports from `state/copilot_sdk_smoke_test.py`.
3. Run targeted smoke validation for supported modes.
4. Record outcomes and recommend exactly one next task.

## Expected files to change
- `state/llm_client.py`
- `state/copilot_sdk_smoke_test.py`
- `state/migration_iterations/iter_027/*.md`
