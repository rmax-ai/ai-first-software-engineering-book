# Next iteration recommendation

## Recommended task
Add structured trace-summary logging in `state/kernel.py` and validate with targeted smoke coverage.

## Why this is next
This is the smallest implementation step that improves observability while preserving current interfaces and creating measurable signals for later eval alignment.

## Acceptance criteria
- Add deterministic trace-summary emission points in `state/kernel.py` behind existing execution flow.
- Add/adjust targeted checks in `state/copilot_sdk_smoke_test.py` and/or `state/copilot_sdk_uv_smoke.py` proving the new summaries appear and remain stable.
- Record expected signal touchpoints for later eval wiring in `evals/` and `state/metrics.json` notes within the next iteration artifacts.

## Expected files to touch
- `state/kernel.py`
- `state/copilot_sdk_smoke_test.py`
- `state/copilot_sdk_uv_smoke.py`
- `state/feature_iterations/iter_002/*`
