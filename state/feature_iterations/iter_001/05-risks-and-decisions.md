# Risks and decisions

## Risks discovered
- Planning-only output may drift from current code if implementation is delayed.
- Eval contract updates can introduce false positives if metric expectations are not synchronized.

## Decisions made
- Chose a planning-first seed iteration exactly as required by `prompts/incremental-improvements/execute.md`.
- Kept scope to one smallest unfinished task: produce a harness-improvement backlog and handoff artifacts.

## Deferred intentionally
- No harness code changes in `state/` during this iteration.
- No eval YAML modifications until implementation iterations begin.
