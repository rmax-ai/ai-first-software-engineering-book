# Next iteration

## Recommended next task
Add a deterministic parity guard mode that verifies both kernel and non-kernel trace-summary fixture root-cleanup and fixture-cleanup parity modes are listed exactly once in generated usage examples.

## Why it is next
Mode behavior parity is now covered for both cleanup variants; generated usage parity listing is the adjacent deterministic documentation guard.

## Concrete acceptance criteria
1. Add one mode in `state/copilot_sdk_smoke_test.py` that asserts both parity mode names appear exactly once in generated usage examples.
2. Keep existing parity execution modes unchanged.
3. Record validation evidence under `state/feature_iterations/iter_070/04-validation.md`.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_070/*.md`

