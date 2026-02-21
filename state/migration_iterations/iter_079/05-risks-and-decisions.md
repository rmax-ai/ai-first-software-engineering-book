# Risks and Decisions

## Risks discovered
- Historical migration artifacts contain many near-duplicate command-text snippets, making accidental broad edits a risk.

## Decisions made and trade-offs
- Chose a strict one-line patch in `state/migration_iterations/iter_077/01-task.md` to minimize churn and preserve historical context.
- Used targeted `rg` plus scoped `git diff` validation instead of broader checks because only markdown command wording changed.

## Anything intentionally deferred
- Deferred normalization of similar escaped fallback-error snippets in other iteration folders to future single-task iterations.
