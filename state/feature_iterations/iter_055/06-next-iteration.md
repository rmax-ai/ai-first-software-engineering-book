# Next iteration

## Recommended next task
Add a deterministic smoke mode fixture builder inside `state/copilot_sdk_uv_smoke.py` so phase-trace validation no longer depends on ad hoc repository fixture files.

## Why it is next
This keeps observability coverage reproducible while removing temporary fixture management overhead and reducing risk of stale test artifacts.

## Concrete acceptance criteria
1. Add a built-in fixture path for trace-summary mode that can generate/read minimal synthetic metrics+trace data in a controlled location.
2. Ensure the command `uv run python state/copilot_sdk_uv_smoke.py --mode trace-summary` can pass deterministically without relying on pre-created repository files.
3. Document the new deterministic smoke invocation in the next iteration validation artifact.

## Expected files to touch
- `state/copilot_sdk_uv_smoke.py`
- `state/feature_iterations/iter_056/*.md`
