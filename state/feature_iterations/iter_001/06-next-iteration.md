# Next Iteration Recommendation

## Recommended next task
Implement structured trace lifecycle logging in `state/kernel.py` and validate it via smoke coverage updates.

## Why this is next
Trace lifecycle visibility is the foundational dependency for confidently evolving role-IO scaffolds and eval gating without regressions.

## Acceptance criteria
- Add deterministic trace lifecycle event emission (start, tool-call, validation, completion/failure) in `state/kernel.py`.
- Add/adjust smoke mode(s) in `state/copilot_sdk_uv_smoke.py` that assert lifecycle event presence and ordering.
- Document verification evidence from `uv run python state/copilot_sdk_uv_smoke.py` in the new iteration `04-validation.md`.

## Expected files to touch
- `state/kernel.py`
- `state/copilot_sdk_uv_smoke.py`
- `state/feature_iterations/iter_002/03-execution.md`
- `state/feature_iterations/iter_002/04-validation.md`
