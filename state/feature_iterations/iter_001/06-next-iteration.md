# Next iteration recommendation

## Recommended next task

Implement deterministic trace logging boundaries in `state/kernel.py` and add targeted smoke coverage for those signals.

## Why this is next

This unlocks the highest-value observability feature from the new backlog and creates a concrete base for later role-IO and eval alignment work.

## Acceptance criteria

1. `state/kernel.py` emits bounded, deterministic trace events for major loop phases without changing public CLI behavior.
2. `state/copilot_sdk_uv_smoke.py` adds assertions that verify the new trace boundaries.
3. Validation includes running `uv run python state/copilot_sdk_uv_smoke.py` with recorded pass/fail evidence.
4. Iteration artifacts are updated with exact commands, outputs, and risk notes.

## Expected files to touch

- `state/kernel.py`
- `state/copilot_sdk_uv_smoke.py`
- `state/feature_iterations/iter_002/01-task.md`
- `state/feature_iterations/iter_002/02-plan.md`
- `state/feature_iterations/iter_002/03-execution.md`
- `state/feature_iterations/iter_002/04-validation.md`
- `state/feature_iterations/iter_002/05-risks-and-decisions.md`
- `state/feature_iterations/iter_002/06-next-iteration.md`
- `state/feature_iterations/iter_002/07-summary.md`
