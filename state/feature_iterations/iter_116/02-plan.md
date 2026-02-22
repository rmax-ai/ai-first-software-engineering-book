# Plan

1. Add one dedicated uniqueness guard handler in `state/copilot_sdk_smoke_test.py` that counts occurrences of the long-form `...-uniqueness-adjacency-guard` mode in `TRACE_SUMMARY_MODE_SPECS`.
2. Register a corresponding `...-uniqueness-adjacency-uniqueness-guard` mode tuple in `TRACE_SUMMARY_MODE_SPECS` with deterministic wording.
3. Run the targeted smoke command for the new mode and capture the exact PASS output.
4. Record execution, validation, risks, and next-step handoff in `state/feature_iterations/iter_116/0*-*.md`.

## Files expected to change
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_116/01-task.md`
- `state/feature_iterations/iter_116/02-plan.md`
- `state/feature_iterations/iter_116/03-execution.md`
- `state/feature_iterations/iter_116/04-validation.md`
- `state/feature_iterations/iter_116/05-risks-and-decisions.md`
- `state/feature_iterations/iter_116/06-next-iteration.md`
- `state/feature_iterations/iter_116/07-summary.md`
