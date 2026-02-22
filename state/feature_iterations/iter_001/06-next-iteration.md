# Next Iteration Recommendation

## Recommended next task
Implement deterministic trace-summary enrichment in `state/kernel.py` with matching smoke assertions.

## Why this is next
- It is the smallest executable slice from the plan that directly improves harness observability.
- It can be validated with focused smoke execution before touching eval contract files.

## Acceptance criteria
- Add a minimal trace-summary enrichment helper path in `state/kernel.py` that records deterministic per-loop summary fields.
- Update `state/copilot_sdk_uv_smoke.py` with one targeted mode that asserts the new trace-summary fields.
- Execute `uv run python state/copilot_sdk_uv_smoke.py` with the targeted mode and record pass/fail evidence in the new iteration artifacts.
- Keep public CLI/kernel interfaces unchanged.

## Expected files to touch
- `state/kernel.py`
- `state/copilot_sdk_uv_smoke.py`
- `state/feature_iterations/iter_002/03-execution.md`
- `state/feature_iterations/iter_002/04-validation.md`
