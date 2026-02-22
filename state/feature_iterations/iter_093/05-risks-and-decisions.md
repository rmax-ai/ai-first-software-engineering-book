# Risks and decisions

## Risks discovered
- The delegation assertion is source-string based and depends on wrappers continuing to call the helper with a recognizable function name.

## Decisions made and trade-offs
- Reused `inspect.getsource(...)` to match existing wrapper regression-guard patterns for deterministic and minimal-diff enforcement.
- Scoped the guard to mode names prefixed with `usage-examples-duplicate-count-mode-coverage-guard` to avoid false positives from unrelated modes.

## Anything intentionally deferred
- No AST-based enforcement was added because current source-level guards already meet this repository's deterministic smoke pattern.
