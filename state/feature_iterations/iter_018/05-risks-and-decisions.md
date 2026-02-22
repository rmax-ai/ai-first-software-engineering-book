# Risks and decisions

## Risks discovered
- Docstring formatting changes could invalidate strict string matching if future rendering conventions change.

## Decisions made
- Used a minimal deterministic substring check (`- <mode>:`) per mode to guard coverage while avoiding brittle full-doc snapshots.
- Added one new mode only; existing mode names, handlers, and help derivation remain unchanged.

## Deferred items
- No broader snapshot testing for full docstring layout in this iteration.
