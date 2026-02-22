# Next iteration recommendation

## Recommended task
Implement deterministic trace-summary observability hooks in `state/kernel.py` with matching smoke coverage.

## Why this is next
It is the smallest code slice that enables measurable harness visibility and unlocks follow-on template/eval alignment work.

## Acceptance criteria
- Add a focused helper in `state/kernel.py` that emits stable trace-summary fields for each loop.
- Add/extend one smoke mode in `state/copilot_sdk_uv_smoke.py` that asserts those fields are present and ordered.
- Update execution docs in the new iteration folder with exact verification command/output.

## Expected files to touch
- `state/kernel.py`
- `state/copilot_sdk_uv_smoke.py`
- `state/feature_iterations/iter_002/*`
