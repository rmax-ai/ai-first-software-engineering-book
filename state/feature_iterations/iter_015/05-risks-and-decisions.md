# Risks and decisions

## Risks discovered
- The top-of-file usage text still manually documents modes, so future mode additions can drift from runtime mode tables.

## Decisions and trade-offs
- Scoped this iteration to shutdown mode wiring only, matching the prior iteration handoff and minimizing behavior risk.
- Kept existing stub/sdk/bootstrap and trace-summary structure unchanged outside shared-table integration.

## Deferred items
- Optionally table-drive remaining non-shutdown/non-trace mode metadata for full `--mode` help consolidation.
