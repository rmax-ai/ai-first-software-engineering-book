# Next iteration recommendation

## Recommended task
Implement deterministic trace summary fields in `state/kernel.py` and cover them with targeted smoke assertions.

## Why this is next
This is the smallest executable slice from the plan that unlocks observability and provides concrete signals for later role I/O and eval contract updates.

## Acceptance criteria
- Add trace summary fields in kernel outputs for step-level guard/eval decisions without changing existing public CLI entrypoints.
- Add/extend a focused smoke mode in `state/copilot_sdk_uv_smoke.py` that asserts the new trace fields are present and ordered deterministically.
- Record validation with `uv run python state/copilot_sdk_uv_smoke.py --mode <new-mode>` (or equivalent targeted harness command) and capture pass/fail evidence.

## Expected files to touch
- `state/kernel.py`
- `state/copilot_sdk_uv_smoke.py`
- `state/feature_iterations/iter_002/0{1..7}-*.md`
