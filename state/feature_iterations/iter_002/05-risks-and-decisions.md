# Risks and decisions

## Risks discovered

- Local Python runtime lacks `PyYAML`, so full CLI runtime execution could not be completed without UV environment access.

## Decisions made

- Chose the smallest safe scope: tracepoint instrumentation only.
- Added append-only JSONL trace events to avoid schema churn in `ledger.json` / `metrics.json` during this iteration.

## Deferred

- Wiring tracepoint aggregates into `state/metrics.json`.
- Adding deterministic guard signal expansion in the ledger payload.
