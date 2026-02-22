# Next iteration recommendation

## Recommended task
Implement kernel trace-summary observability and smoke assertions.

## Why this is next
It is the smallest implementation slice that exercises the planned feature/test/eval loop and produces measurable evidence for future eval contract updates.

## Acceptance criteria
- Add deterministic trace-summary fields in `state/kernel.py` for key loop stages.
- Update `state/copilot_sdk_uv_smoke.py` to assert new trace-summary fields are present and well-formed.
- Run `uv run python state/copilot_sdk_uv_smoke.py` and record pass/fail evidence.
- Document whether `evals/*.yaml` changes are required based on observed outputs.

## Expected files to touch
- `state/kernel.py`
- `state/copilot_sdk_uv_smoke.py`
- `state/feature_iterations/iter_002/04-validation.md`
