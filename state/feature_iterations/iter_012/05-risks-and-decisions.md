# Risks and Decisions

## Risks discovered
- CLI mode help text is long and easy to desynchronize from choices and dispatch.

## Decisions made
- Followed existing pattern by wiring the new mode across usage docs, mode list, help text, and dispatcher.
- Validated the new mode plus adjacent trace-summary modes to reduce regression risk.

## Deferred
- No argparse help-text refactor was performed to keep this iteration minimal.
