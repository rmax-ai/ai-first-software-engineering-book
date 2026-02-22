# Next Iteration Recommendation

## Task
Implement deterministic trace-summary logging enhancements in `state/kernel.py` with backward-safe output shape guarantees.

## Why this is next
It unlocks the highest observability gain for subsequent harness changes while providing a focused, testable vertical slice touching core orchestration behavior.

## Acceptance criteria
- Add trace-summary emission points in `state/kernel.py` for key loop decisions and outcomes.
- Preserve existing public interfaces and current successful execution paths.
- Add/extend deterministic smoke coverage in `state/copilot_sdk_uv_smoke.py` that validates summary presence and shape.
- Run targeted verification commands and record outputs in the new iteration `04-validation.md`.

## Expected files to touch
- `state/kernel.py`
- `state/copilot_sdk_uv_smoke.py`
- `state/feature_iterations/iter_002/*`
