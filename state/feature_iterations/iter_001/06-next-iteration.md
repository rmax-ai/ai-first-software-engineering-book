# Recommended next task

## Task

Implement deterministic trace-summary observability guard in `state/kernel.py` and prove it with one new smoke mode in `state/copilot_sdk_uv_smoke.py`.

## Why this is next

The plan prioritizes feature visibility first; trace-summary guardrails create measurable signals that later role-template and eval updates can build on.

## Acceptance criteria

1. `state/kernel.py` emits or validates one additional deterministic trace-summary signal without changing existing public CLI behavior.
2. `state/copilot_sdk_uv_smoke.py` adds exactly one mode that fails before the kernel change and passes after it.
3. Validation evidence includes `uv run python state/copilot_sdk_uv_smoke.py --mode <new-mode>` with captured pass/fail outcome.
4. Iteration artifacts document touched files and rationale with minimal diffs.

## Expected files to touch

- `state/kernel.py`
- `state/copilot_sdk_uv_smoke.py`
- `state/feature_iterations/iter_002/03-execution.md`
- `state/feature_iterations/iter_002/04-validation.md`
