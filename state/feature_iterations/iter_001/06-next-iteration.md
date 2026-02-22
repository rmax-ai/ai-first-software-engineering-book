# Recommended next task
Implement deterministic trace observability wiring in the state harness.

## Why this is next
- It is the highest-value foundational change for validating subsequent harness behavior improvements.
- It enables stronger smoke/eval assertions before broader template or evaluator refactors.

## Acceptance criteria
- Add explicit per-phase trace summary fields in `state/kernel.py` without changing existing public CLI arguments.
- Extend `state/copilot_sdk_uv_smoke.py` with deterministic checks that fail when new trace summary fields are missing or malformed.
- Update at least one relevant eval contract in `evals/` to assert the new observable signal shape.
- Validate with `uv run python state/copilot_sdk_uv_smoke.py` and record command outcome in next iteration artifacts.

## Expected files to touch
- `state/kernel.py`
- `state/copilot_sdk_uv_smoke.py`
- `evals/chapter-quality.yaml`
- `state/feature_iterations/iter_002/*`
