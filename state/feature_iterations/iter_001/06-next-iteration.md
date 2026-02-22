# Next Iteration Recommendation

## Recommended next task

Implement deterministic trace diagnostics in `state/kernel.py` with targeted validation hooks.

## Why this is next

It is the highest-impact feature slice from the new plan and unblocks downstream smoke/eval enhancements by producing stable, machine-checkable signals.

## Acceptance criteria

1. `state/kernel.py` emits explicit phase-level diagnostic fields for guardrail/budget outcomes.
2. Added targeted tests for new diagnostics behavior in `state/` test surface.
3. `uv run python state/copilot_sdk_uv_smoke.py` includes at least one mode asserting the new diagnostic shape.
4. Iteration artifacts capture command evidence and pass/fail outcomes.

## Expected files to touch

- `state/kernel.py`
- `state/copilot_sdk_uv_smoke.py`
- `state/` test files related to kernel behavior
- `state/feature_iterations/iter_002/01-task.md` to `07-summary.md`
