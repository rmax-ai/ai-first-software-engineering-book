# Validation

## Verification commands
- `ls -1 state/feature_iterations/iter_001`
- `rg -n "^# " state/feature_iterations/iter_001/*.md`
- `rg -n "state/kernel.py|state/role_io_templates.py|state/copilot_sdk_uv_smoke.py|evals/" state/feature_iterations/iter_001/*.md`

## Observed results
- Iteration folder contains all seven required files (`01-task.md` through `07-summary.md`).
- Every artifact is markdown and has a top-level heading.
- Planning artifacts explicitly reference required harness and eval paths.

## Acceptance criteria status
- Criteria 1 (features/tests/evals plan): **PASS**
- Criteria 2 (required target files mentioned): **PASS**
- Criteria 3 (single next task with criteria): **PASS**
