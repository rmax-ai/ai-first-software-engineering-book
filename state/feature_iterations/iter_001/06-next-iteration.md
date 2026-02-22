# Next Iteration Recommendation

## Task
Implement deterministic trace checkpoint summaries in `state/kernel.py` and validate them with a focused UV smoke test extension.

## Why this is next
The seed plan identified trace observability as the highest-leverage foundation; implementing it first improves diagnostics for every subsequent harness change.

## Acceptance criteria
- `state/kernel.py` emits structured checkpoint summaries at key loop boundaries without changing existing public CLI behavior.
- `state/copilot_sdk_uv_smoke.py` includes at least one mode that asserts checkpoint summary presence and stable ordering.
- Validation includes running `uv run python state/copilot_sdk_uv_smoke.py --mode <new-mode>` with captured pass/fail evidence in the next iteration’s `04-validation.md`.

## Expected files to touch
- `state/kernel.py`
- `state/copilot_sdk_uv_smoke.py`
- `state/feature_iterations/iter_002/01-task.md`
- `state/feature_iterations/iter_002/02-plan.md`
- `state/feature_iterations/iter_002/03-execution.md`
- `state/feature_iterations/iter_002/04-validation.md`
