# Table-drive trace-summary smoke mode specs

## Why this task now
`iter_059/06-next-iteration.md` prioritized replacing repetitive trace-summary mode branching with one shared mode-spec structure.

## Acceptance criteria
1. Add one mode-spec map for `trace-summary`, `trace-summary-malformed-phase`, `trace-summary-malformed-phase-payload`, and `trace-summary-missing-phase`.
2. Reuse that same map for argparse `--mode` choices and runtime dispatch in `main_async`.
3. Re-run all four trace-summary smoke modes and record results in `iter_060/04-validation.md`.
