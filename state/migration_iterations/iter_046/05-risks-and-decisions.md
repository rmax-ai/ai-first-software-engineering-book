# Risks and Decisions

## Risks discovered
- M1 live-runtime behavior is still unverified; migration confidence remains limited to deterministic/stub paths.

## Decisions made and trade-offs
- Kept scope to one task and captured hard failure evidence rather than adding unrelated environment bootstrap changes.
- Deferred remediation to next iteration with a bounded unblock step.

## Deferred items
- Install/enable the Copilot SDK runtime dependency and rerun the live smoke mode.
