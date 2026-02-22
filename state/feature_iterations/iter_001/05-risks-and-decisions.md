# Risks and decisions

## Risks discovered
- Kernel observability and smoke/eval updates can drift if implemented separately.
- Changes to eval contracts may increase false positives without synchronized fixture updates.

## Decisions and trade-offs
- Chose planning-only scope to satisfy seed iteration contract with minimal diff.
- Prioritized a single next task that couples kernel behavior with smoke verification to reduce drift risk.

## Deferred intentionally
- No code changes in `state/` or `evals/` this iteration; implementation is deferred to the next iteration task.
