# Risks and Decisions

## Risks discovered
- Kernel validation mutates `state/ledger.json` and `state/metrics.json` heavily when run repeatedly; this can create large unrelated diffs.
- Live-provider validation still depends on external prerequisites (`COPILOT_API_KEY` or a running local Copilot CLI server).

## Decisions made and trade-offs
- Decision: treat mock regression validation as complete based on artifact and rerun evidence.
- Decision: restore transient ledger/metrics mutations to preserve minimal migration diffs.
- Trade-off: no further chapter-state progression is persisted in this iteration commit.

## Anything intentionally deferred
- Persisting additional kernel runtime state mutations from validation runs.
- Reattempting live-provider smoke without environment prerequisites.
