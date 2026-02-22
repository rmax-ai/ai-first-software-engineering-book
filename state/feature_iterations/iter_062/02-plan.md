# Plan

1. Add a kernel fixture builder in `state/copilot_sdk_uv_smoke.py` that creates an isolated repo under `state/.smoke_fixtures/trace_summary/kernel_repo`.
2. Copy required runtime inputs into the fixture repo (kernel modules, prompts, eval YAMLs, governance files, roadmap, and chapter source), then initialize fixture git metadata.
3. Override fixture ledger chapter eligibility (`status`) to avoid `hold`-state blocker while keeping production `state/ledger.json` untouched.
4. Run kernel from the fixture repo for `--run-kernel-for-trace-summary` and validate trace-summary + phase-trace outputs.
5. Execute all four required smoke commands and capture evidence in validation artifacts.

## Files expected to change
- `state/copilot_sdk_uv_smoke.py`
- `state/feature_iterations/iter_062/01-task.md`
- `state/feature_iterations/iter_062/02-plan.md`
- `state/feature_iterations/iter_062/03-execution.md`
- `state/feature_iterations/iter_062/04-validation.md`
- `state/feature_iterations/iter_062/05-risks-and-decisions.md`
- `state/feature_iterations/iter_062/06-next-iteration.md`
- `state/feature_iterations/iter_062/07-summary.md`
