# Risks and decisions

## Risks discovered
- This long-suffix mode family is error-prone because tiny string differences can break deterministic mode matching.

## Decisions made and trade-offs
- Reused the existing helper instead of further abstraction to keep this iteration minimal and low-risk.
- Kept validation targeted to the adjacent highest-suffix modes for fast, direct confidence in touched behavior.

## Intentionally deferred
- Broader deduplication of mode registration/definitions beyond this final wrapper migration.
