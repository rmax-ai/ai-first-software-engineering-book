# Risks and decisions

## Risks discovered
- The top-of-file usage/mode docstring still lists trace-summary modes manually; future additions could drift from runtime registration.

## Decisions and trade-offs
- Kept non-trace-summary mode wiring unchanged to minimize scope and preserve stable behavior.
- Built only trace-summary help fragment from the new mapping to satisfy this iteration with minimal diff.

## Deferred items
- Optionally derive usage/mode docstring text from mode tables in a later cleanup iteration.
