# Risks and decisions

## Risks discovered
- Long mode-name chains are error-prone for manual edits and can drift in literal strings.

## Decisions made and trade-offs
- Reused the existing guard pattern (count in `TRACE_SUMMARY_MODE_SPECS` plus deterministic PASS string) to minimize behavioral risk and diff size.
- Kept scope to a single requested guard mode; no refactors to naming or helper abstraction were introduced.

## Anything intentionally deferred
- Broader simplification of long mode-name literals remains deferred to future iterations.
