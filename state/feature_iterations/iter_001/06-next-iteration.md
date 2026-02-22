# Next Iteration Recommendation

## Next task
Add structured kernel trace events for deterministic decision points in `state/kernel.py`.

## Why this is next
Trace visibility is the narrowest high-value feature from the plan and enables faster debugging plus clearer validation evidence for later control and eval work.

## Acceptance criteria
- Add a minimal structured trace emitter in `state/kernel.py` for key loop decisions (task selection, validation outcome, completion/abort).
- Ensure trace records are deterministic in shape and written through existing harness logging paths.
- Add/extend targeted smoke coverage in `state/copilot_sdk_uv_smoke.py` (or nearby harness test surface) to assert trace event presence and schema.
- Document any eval hook updates needed in `evals/drift-detection.yaml` or related eval contracts.

## Expected files to touch
- `state/kernel.py`
- `state/copilot_sdk_uv_smoke.py`
- `evals/drift-detection.yaml`
- `state/feature_iterations/iter_002/*`
