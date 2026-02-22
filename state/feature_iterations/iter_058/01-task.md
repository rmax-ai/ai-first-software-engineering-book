# Add non-object phase_trace.payload smoke guard

## Why this task now
`iter_057` recommended hardening `phase_trace.payload` schema checks beyond missing keys, specifically for non-object payload regressions.

## Acceptance criteria
1. Add deterministic smoke coverage that injects non-object `phase_trace.payload` and expects validation failure.
2. Keep `--mode trace-summary` and `--mode trace-summary-malformed-phase` passing.
3. Record command evidence for all exercised modes in `state/feature_iterations/iter_058/04-validation.md`.
