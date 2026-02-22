# Next Iteration Recommendation

## Recommended next task (exactly one)
Implement deterministic trace-decision observability plumbing in `state/kernel.py` and validate it with a focused smoke assertion.

## Why this is next
- It is the smallest high-impact harness improvement and creates measurable signals for later role-template and eval wiring work.

## Acceptance criteria
- Add a minimal, explicit trace summary field for per-loop decision state in `state/kernel.py`.
- Add one targeted smoke mode/assertion in `state/copilot_sdk_uv_smoke.py` validating the new field is emitted.
- Update one relevant eval contract (`evals/drift-detection.yaml` or `evals/chapter-quality.yaml`) to document/check the new signal.
- Run targeted verification with `uv run python state/copilot_sdk_uv_smoke.py` (or narrowed mode) and record observed result.

## Expected files to touch
- `state/kernel.py`
- `state/copilot_sdk_uv_smoke.py`
- `evals/drift-detection.yaml` (or `evals/chapter-quality.yaml`)
- `state/feature_iterations/iter_002/0{1..7}-*.md`
