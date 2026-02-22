# Risks and decisions

## Risks discovered
- Parity mode reuses existing handlers, so troubleshooting still depends on reading preceding PASS/FAIL output lines for side-specific context.

## Decisions made and trade-offs
- Composed existing kernel and non-kernel fixture-cleanup handlers directly to minimize diff size and preserve current behavior.
- Kept the new mode focused on parity only, deferring richer diagnostics to avoid scope growth.

## Deferred
- Add explicit side-labeled failure summaries inside parity mode output.

