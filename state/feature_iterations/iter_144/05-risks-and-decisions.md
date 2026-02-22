# Risks and decisions

## Risks discovered
- Long mode-name strings are fragile; minor copy errors can silently target the wrong adjacency pair.

## Decisions made and trade-offs
- Reused existing assertion and registration patterns instead of introducing helper abstractions to keep this one-task diff small.
- Kept the test scope targeted to the new mode to reduce runtime and isolate regressions to the changed surface.

## Deferred
- Broader refactors to reduce long-mode string duplication remain deferred.
