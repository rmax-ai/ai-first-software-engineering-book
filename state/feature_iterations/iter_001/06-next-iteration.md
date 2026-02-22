# Recommended next task
Implement deterministic trace logging scaffolds in `state/kernel.py` and propagate structured fields needed by smoke/eval checks.

## Why this is next
- It is the smallest implementation slice that unlocks observability improvements and testable eval signals.
- It directly operationalizes the planning backlog without broad interface churn.

## Acceptance criteria
1. `state/kernel.py` emits structured trace records for each phase transition with stable keys.
2. `state/copilot_sdk_uv_smoke.py` adds or updates one deterministic assertion that validates the new trace shape.
3. Validation evidence includes at least one `uv run python state/copilot_sdk_uv_smoke.py --mode <targeted-mode>` command result.

## Expected files to touch
- `state/kernel.py`
- `state/copilot_sdk_uv_smoke.py`
- `state/feature_iterations/iter_002/03-execution.md`
- `state/feature_iterations/iter_002/04-validation.md`
