# Plan

1. Update `state/copilot_sdk_smoke_test.py` usage header to replace `python ...` with `uv run python ...`.
2. Update migration guidance in `state/copilot-sdk-migration-plan.md` to show the same command style.
3. Run the smoke test via `uv run python state/copilot_sdk_smoke_test.py --mode stub`.
4. Record execution and validation evidence in this iteration folder.

## Files expected to change
- `state/copilot_sdk_smoke_test.py`
- `state/copilot-sdk-migration-plan.md`
- `state/migration_iterations/iter_048/*.md`
