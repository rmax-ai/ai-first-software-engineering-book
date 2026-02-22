# Risks and decisions

## Risks discovered
- If root-cleanup semantics diverge later, parity mode will fail but may not indicate which side regressed without checking preceding output.

## Decisions made and trade-offs
- Implemented parity by composing existing mode handlers directly to maximize reuse and preserve behavior.
- Kept diagnostics minimal to avoid scope creep and maintain a small diff.

## Deferred
- Richer per-side failure labeling inside parity mode output.

