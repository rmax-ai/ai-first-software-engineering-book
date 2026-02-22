# Next Iteration Recommendation

## Task
Implement kernel trace-summary observability improvements in `state/kernel.py`.

## Why this is next
It is the smallest high-impact backlog item: improved trace summaries make subsequent harness changes easier to verify and debug while preserving current interfaces.

## Acceptance criteria
- Add deterministic, concise trace summary output for key loop phases and failure points in `state/kernel.py`.
- Cover the new trace behavior with targeted harness tests or smoke assertions in `state/copilot_sdk_uv_smoke.py`.
- Validate no regressions against existing eval gates (`evals/chapter-quality.yaml`, `evals/style-guard.yaml`, `evals/drift-detection.yaml`) and document evidence.

## Expected files to touch
- `state/kernel.py`
- `state/copilot_sdk_uv_smoke.py`
- `state/feature_iterations/iter_002/0{1..7}-*.md` (next iteration artifacts)
