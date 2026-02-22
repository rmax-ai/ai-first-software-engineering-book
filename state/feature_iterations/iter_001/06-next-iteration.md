# Next iteration recommendation

## Task
Implement deterministic trace-summary observability in `state/kernel.py` with corresponding smoke verification in `state/copilot_sdk_uv_smoke.py`.

## Why next
This delivers the smallest implementation slice from the new backlog while creating direct, testable evidence for harness behavior and establishing a pattern for later role-template/eval enhancements.

## Acceptance criteria
- `state/kernel.py` emits stable trace-summary fields for each required phase in a deterministic structure.
- `state/copilot_sdk_uv_smoke.py` adds/updates one smoke mode that fails when trace-summary structure is missing or malformed.
- Validation includes `uv run python state/copilot_sdk_uv_smoke.py --mode <new-or-updated-mode>` with captured pass/fail evidence in iteration artifacts.

## Expected files to touch
- `state/kernel.py`
- `state/copilot_sdk_uv_smoke.py`
- `state/feature_iterations/iter_002/04-validation.md`
