# Task

## Selected task title
Migrate the final duplicate-count coverage-guard wrapper to `_run_usage_examples_duplicate_count_mode_coverage_guard(...)`.

## Why this task now
`state/feature_iterations/iter_090/06-next-iteration.md` prioritized continuing this wrapper-reduction track, and one direct wrapper implementation remained.

## Acceptance criteria
1. Replace the remaining direct implementation of `run_usage_examples_duplicate_count_mode_coverage_guard*` with a helper call.
2. Preserve the touched PASS output string exactly.
3. Run targeted smoke modes for the 22-guard and 23-guard duplicate-count coverage checks.
