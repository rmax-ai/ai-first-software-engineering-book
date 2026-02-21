# Task

## Selected task title
Run deterministic kernel regression in `mock` mode and verify ledger/metrics usage schema stability.

## Why this task now
`iter_008` recommended kernel-level deterministic regression to validate migration safety beyond unit-level adapter checks.

## Acceptance criteria for this iteration
- Execute one kernel run with `--llm-provider mock`.
- Confirm planner → writer → critic flow evidence (`_llm_trace`) is produced.
- Confirm `state/ledger.json` and `state/metrics.json` usage fields remain numeric and non-negative.
