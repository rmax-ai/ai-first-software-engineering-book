# Risks and Decisions

## Risks discovered
- Helper currently migrates parity cleanup guard modes only; other mode-coverage guards still duplicate lookup logic.

## Decisions made and trade-offs
- Scoped migration strictly to parity cleanup guard modes to satisfy the single-task iteration requirement.
- Kept assertion text and behavior unchanged to avoid changing diagnostics.

## Intentionally deferred
- Broader helper migration for all remaining mode-coverage guards.
