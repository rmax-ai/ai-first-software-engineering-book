# Add kernel-run trace-summary smoke coverage

## Why this task now
`iter_060/06-next-iteration.md` prioritized validating `--run-kernel-for-trace-summary` across all trace-summary modes to catch integration drift.

## Acceptance criteria
1. Execute kernel-backed smoke commands for `trace-summary`, `trace-summary-malformed-phase`, `trace-summary-malformed-phase-payload`, and `trace-summary-missing-phase`.
2. Record pass/fail results for all four commands in `iter_061/04-validation.md`.
3. Keep scope to smoke verification and iteration artifacts unless a concrete integration bug is identified.
