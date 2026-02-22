# Next Iteration Recommendation

## Task
Implement deterministic phase-trace observability in `state/kernel.py` and validate it via smoke coverage updates.

## Why this is next
The backlog prioritizes visibility and execution determinism first; trace improvements unlock safer follow-on changes to role-IO scaffolds and eval contracts.

## Acceptance criteria
1. `state/kernel.py` emits structured phase trace records for each major loop phase with stable keys.
2. `state/copilot_sdk_uv_smoke.py` gains one focused mode validating presence and shape of phase trace output.
3. `04-validation.md` for that iteration includes executed `uv run python state/copilot_sdk_uv_smoke.py --mode <new-mode>` evidence.

## Expected files to touch
- `state/kernel.py`
- `state/copilot_sdk_uv_smoke.py`
- `state/feature_iterations/iter_002/04-validation.md`
