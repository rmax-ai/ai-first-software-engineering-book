# Risks and Decisions

## Risks discovered
- Historical migration artifacts can be accidentally over-edited if normalization is done via broad replacements.

## Decisions made and trade-offs
- Performed a single-line patch in only `state/migration_iterations/iter_081/01-task.md` to minimize churn.
- Used targeted `rg` plus scoped git diff evidence instead of wider validation because no runtime code changed.

## Anything intentionally deferred
- Remaining wording normalizations in adjacent historical iteration artifacts were deferred to the next single-task iteration.
