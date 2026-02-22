# Plan

1. Define the feature backlog for deterministic harness improvements in:
   - `state/kernel.py`
   - `state/role_io_templates.py`
   - `state/copilot_sdk_uv_smoke.py`
2. Specify observability and control upgrades for `state/kernel.py`:
   - richer structured trace points for loop phases and gate outcomes
   - deterministic budget/failure reason emission for easier diagnosis
   - explicit invariants for heading-preservation and diff-cap checks
3. Specify role I/O scaffold refinements in `state/role_io_templates.py`:
   - tighter template contracts for planner/writer/critic payloads
   - clearer required/optional fields to reduce ambiguous role exchanges
4. Specify smoke-test coverage upgrades in `state/copilot_sdk_uv_smoke.py`:
   - targeted modes that assert new trace and role-IO invariants
   - guard tests proving deterministic ordering and failure messaging
5. Map eval impacts under `evals/*.yaml`:
   - identify chapter-quality/style/drift rules impacted by new logging and deterministic controls
   - define expected observable signals so regressions are caught by eval gates
6. Define rollout order for later iterations:
   - implement kernel observability/control helpers first
   - add/update smoke tests
   - update eval configs/docs only where needed
   - run targeted verification and record evidence in each iteration folder

## Files expected to change in later iterations
- `state/kernel.py`
- `state/role_io_templates.py`
- `state/copilot_sdk_uv_smoke.py`
- `evals/chapter-quality.yaml`
- `evals/style-guard.yaml`
- `evals/drift-detection.yaml`
