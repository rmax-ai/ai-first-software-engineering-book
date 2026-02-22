# Task

## Selected task title
Add a deterministic parity guard mode for trace-summary fixture root cleanup.

## Why this task now
`iter_067/06-next-iteration.md` prioritized a single smoke command that proves both kernel and non-kernel root-cleanup paths pass together.

## Acceptance criteria for this iteration
1. Add one mode in `state/copilot_sdk_smoke_test.py` that runs both root-cleanup guards and fails if either path fails.
2. Keep existing standalone root-cleanup modes unchanged.
3. Record validation evidence in `state/feature_iterations/iter_068/04-validation.md`.

