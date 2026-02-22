# Risks and decisions

## Risks discovered
- The mode names are long and similar, so copy/paste drift could point the new uniqueness check at the wrong guard identifier.

## Decisions made and trade-offs
- Reused the existing exact-count guard pattern and only introduced one new handler + one tuple registration to keep the diff minimal.
- Kept existing ordering/adjacency semantics untouched to avoid changing behavior beyond the requested uniqueness hardening.

## Anything intentionally deferred
- Deferred adding another adjacency guard for the new uniqueness mode; the next iteration can add that order-hardening step.
