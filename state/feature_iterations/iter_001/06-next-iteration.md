# Recommended next task

## Task
Define and implement deterministic trace-summary enrichment in `state/kernel.py`.

## Why this is next
- It unlocks measurable observability improvements that downstream template and smoke-test work can validate.
- It creates the concrete data contract needed before touching eval expectations.

## Acceptance criteria
1. `state/kernel.py` emits a stable trace-summary structure with explicit fields for phase timings, tool usage counts, and guardrail outcomes.
2. Existing kernel behavior remains unchanged aside from additive trace data.
3. A targeted verification run demonstrates the new trace-summary fields are present and well-formed.

## Expected files to touch
- `state/kernel.py`
- `state/copilot_sdk_uv_smoke.py` (only if needed for targeted verification)
- `state/feature_iterations/iter_002/04-validation.md` (evidence capture)

