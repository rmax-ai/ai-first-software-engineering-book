# Next iteration recommendation

## Task
Implement deterministic trace and budget observability scaffolding in `state/kernel.py` with matching smoke validation hooks.

## Why this is next
It is the highest-leverage first implementation step from the new plan because it establishes measurable runtime signals that later role-I/O and eval updates can consume.

## Acceptance criteria
- Add minimal, explicit trace fields for iteration budget usage and decision checkpoints in `state/kernel.py`.
- Extend `state/copilot_sdk_uv_smoke.py` to assert the new trace fields are emitted in at least one deterministic scenario.
- Record targeted verification commands/results in the new iteration artifacts, including `uv run python state/copilot_sdk_uv_smoke.py`.

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
