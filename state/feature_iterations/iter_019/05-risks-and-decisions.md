# Risks and Decisions

## Risks discovered
- Help text formatting could drift again if future code bypasses shared mode metadata.
- Long comma-separated help text may become less readable as modes continue growing.

## Decisions made and trade-offs
- Decision: factor mode-help creation into `_build_mode_help(...)` and reuse it in `main()` and guard mode.
- Trade-off: kept current comma-separated help format to avoid behavioral churn in this iteration.

## Intentionally deferred
- Any argparse UX redesign (e.g., multiline/custom formatter help output).
- Any broader refactor of smoke mode grouping or CLI option structure.
