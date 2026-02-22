# Risks and Decisions

## Risks discovered
- Kernel-run smoke coverage is currently blocked when the default chapter is in `hold` status.
- Without a deterministic eligible chapter fixture, this integration path can regress silently.

## Decisions made and trade-offs
- Chose not to mutate `state/ledger.json` chapter status just to force a passing smoke run.
- Captured explicit blocking evidence and deferred implementation to a focused follow-up task.

## Intentionally deferred
- Adding an isolated eligible-ledger fixture path for kernel-run smoke commands.
