# Risks and decisions

## Risks discovered
- Plan quality risk: if future work does not keep scope small, harness changes could sprawl across kernel and evals.
- Verification risk: adding observability may increase noise unless deterministic assertions are explicitly defined.

## Decisions made and trade-offs
- Chose a planning-only first iteration per prompt seed requirements instead of code changes.
- Prioritized explicit mapping between features, tests, and eval gates to reduce ambiguity in later implementation.

## Intentionally deferred
- Actual code changes in `state/kernel.py`, `state/role_io_templates.py`, smoke scripts, and eval YAML updates are deferred to the next iteration.
