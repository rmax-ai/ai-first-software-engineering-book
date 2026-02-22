# Task

## Selected task title
Add a deterministic parity guard mode for trace-summary fixture cleanup (non-root).

## Why this task now
`iter_068/06-next-iteration.md` prioritized parity coverage for the remaining non-root fixture-cleanup symmetry gap.

## Acceptance criteria for this iteration
1. Add one mode in `state/copilot_sdk_smoke_test.py` that runs both fixture-cleanup guards and fails if either path fails.
2. Keep existing standalone fixture-cleanup modes unchanged.
3. Record validation evidence in `state/feature_iterations/iter_069/04-validation.md`.

