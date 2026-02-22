# Execution

## Commands/tools run
1. `view`/`rg` on `state/copilot_sdk_smoke_test.py` to locate the newest long-form uniqueness-order guard family and registration block.
2. `apply_patch` on `state/copilot_sdk_smoke_test.py` to add one adjacency-order guard runner and one new mode registration.
3. `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-guard` (initial failure, then PASS after moving registration).

## Files changed
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_138/01-task.md`
- `state/feature_iterations/iter_138/02-plan.md`
- `state/feature_iterations/iter_138/03-execution.md`
- `state/feature_iterations/iter_138/04-validation.md`
- `state/feature_iterations/iter_138/05-risks-and-decisions.md`
- `state/feature_iterations/iter_138/06-next-iteration.md`
- `state/feature_iterations/iter_138/07-summary.md`

## Short rationale per change
- Added the smallest new adjacency-order guard mode requested by prior-iteration guidance.
- Kept registration ordering deterministic by placing the new runnable mode away from the two modes whose adjacency is asserted.
- Documented full evidence and handoff artifacts for one completed task iteration.
