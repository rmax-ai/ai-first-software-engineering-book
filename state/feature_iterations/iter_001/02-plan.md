# Iteration plan

1. Inspect `DEVELOPMENT.md` and the seed requirements in `prompts/incremental-improvements/execute.md`.
2. Define a backlog slice for `state/kernel.py`:
   - richer trace summary output for loop evidence,
   - deterministic execution guard checks,
   - clearer failure surfacing for evaluation gates.
3. Define a backlog slice for `state/role_io_templates.py`:
   - template contract tightening for role IO consistency,
   - explicit placeholders that reduce prompt drift.
4. Define verification updates in `state/copilot_sdk_uv_smoke.py`:
   - add/extend deterministic smoke modes proving new trace and guard behavior.
5. Define eval integration:
   - map expected checks to `evals/chapter-quality.yaml`,
   - map style/format guardrails to `evals/style-guard.yaml`,
   - map stability/drift checks to `evals/drift-detection.yaml`.
6. Capture risks, sequencing, and one concrete next implementation task.

## Files expected to change this iteration
- `state/feature_iterations/iter_001/01-task.md`
- `state/feature_iterations/iter_001/02-plan.md`
- `state/feature_iterations/iter_001/03-execution.md`
- `state/feature_iterations/iter_001/04-validation.md`
- `state/feature_iterations/iter_001/05-risks-and-decisions.md`
- `state/feature_iterations/iter_001/06-next-iteration.md`
- `state/feature_iterations/iter_001/07-summary.md`
