# Validation

## Verification commands run
- `rg --files state/feature_iterations/iter_001`
- `rg "state/kernel.py|state/role_io_templates.py|state/copilot_sdk_uv_smoke.py|evals/" state/feature_iterations/iter_001/02-plan.md`

## Observed results
- Iteration folder contains all required seven markdown artifacts.
- Plan explicitly references required harness and eval file paths.

## Acceptance criteria check
- ✅ Plan covers features, tests, and evaluations.
- ✅ Follow-up scope is mapped to required files.
- ✅ Iteration contract (seven artifacts) is complete.

