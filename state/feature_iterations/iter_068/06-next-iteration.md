# Next iteration

## Recommended next task
Add a deterministic parity guard mode that verifies both kernel and non-kernel trace-summary fixture-cleanup (non-root) modes run and pass within one smoke command.

## Why it is next
Root-cleanup parity is now covered; fixture-cleanup parity (without root assertions) remains the adjacent symmetry gap.

## Concrete acceptance criteria
1. Add one mode in `state/copilot_sdk_smoke_test.py` that executes both fixture-cleanup modes and fails if either path fails.
2. Keep existing standalone fixture-cleanup modes unchanged.
3. Record validation evidence under `state/feature_iterations/iter_069/04-validation.md`.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_069/*.md`

