# Risks and decisions

## Risks discovered
- The guard depends on AST parsing of `inspect.getsource(...)`, so heavily dynamic wrapper generation would evade this check.

## Decisions made and trade-offs
- Used AST-based call inspection to validate both helper target and argument shape in a deterministic, low-diff way.
- Kept wrapper selection scoped to `usage-examples-duplicate-count-mode-coverage-guard*` modes to avoid unrelated mode noise.

## Anything intentionally deferred
- Did not add cross-function dataflow checks; this guard remains focused on direct helper delegation signatures.
