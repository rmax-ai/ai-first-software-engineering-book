# Next iteration

## Recommended next task
Add a deterministic parity guard mode that verifies both kernel and non-kernel trace-summary root-cleanup modes run and pass within one smoke command.

## Why it is next
This would lock in symmetry as a single regression guard and reduce risk of future one-sided cleanup regressions.

## Concrete acceptance criteria
1. Add one mode in `state/copilot_sdk_smoke_test.py` that executes both root-cleanup modes and fails if either does not pass.
2. Keep existing standalone root-cleanup modes unchanged.
3. Record validation evidence under `state/feature_iterations/iter_068/04-validation.md`.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_068/*.md`
