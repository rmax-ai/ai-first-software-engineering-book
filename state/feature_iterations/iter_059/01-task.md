# Add missing required `phase_trace` phase smoke guard

## Why this task now
`iter_058/06-next-iteration.md` prioritized explicit fixture-mode coverage for missing required `phase_trace` phases.

## Acceptance criteria
1. Add a deterministic smoke mode that omits one required phase (`evaluation`) and expects failure.
2. Keep `trace-summary`, `trace-summary-malformed-phase`, and `trace-summary-malformed-phase-payload` green.
3. Record command evidence in `iter_059/04-validation.md`.
