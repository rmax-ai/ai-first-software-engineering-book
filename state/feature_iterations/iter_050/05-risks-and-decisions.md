# Risks and decisions

## Risks discovered
- Repetitive long mode names increase typo risk in handler names, mode strings, and registration tuples.
- Incremental coverage expansion can drift if new handler and tuple entries are not added in lockstep.

## Decisions made and trade-offs
- Followed the existing explicit table-driven pattern rather than introducing metaprogramming to keep diff size minimal.
- Kept scope to one new deterministic mode only, matching the prompt and prior handoff guidance.

## Intentionally deferred
- Refactoring repeated duplicate-count coverage handlers into generated helpers.
- Broader cleanup of existing long PASS strings and repetitive descriptions.
