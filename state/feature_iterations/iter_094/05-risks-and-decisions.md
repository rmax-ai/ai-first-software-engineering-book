# Risks and decisions

## Risks discovered
- The new assertion still relies on source-string inspection and can be bypassed by non-standard call indirection patterns.

## Decisions made and trade-offs
- Reused `inspect.getsource(...)` because existing smoke guards in this file use the same deterministic pattern with minimal diff risk.
- Scoped the guard to mode names starting with `usage-examples-duplicate-count-mode-coverage-guard` to avoid unrelated mode noise.

## Anything intentionally deferred
- No AST-based call counting was added; source-level enforcement remains sufficient for current deterministic smoke objectives.
