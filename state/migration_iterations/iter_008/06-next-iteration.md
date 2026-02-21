# Next Iteration Recommendation

## Recommended next task
Run deterministic kernel regression in `mock` mode and verify ledger/metrics usage schema remains stable after SDK lifecycle hardening changes.

## Why it is next
Migration plan test coverage still requires explicit deterministic regression evidence at the kernel level.

## Concrete acceptance criteria
- Execute one kernel run with `--llm-provider mock` successfully.
- Confirm `state/ledger.json` and `state/metrics.json` usage fields remain numeric and non-negative.
- Confirm planner → writer → critic flow still completes with trace artifacts produced.

## Expected files to touch
- `state/migration_iterations/iter_009/*.md`
