# Next Iteration Recommendation

## Next task (exactly one)
Implement deterministic trace summary scaffolding in `state/kernel.py`.

## Why this is next
It unlocks observability needed by all later template, smoke, and eval improvements while remaining a narrowly scoped code change.

## Acceptance criteria
- Add a small, documented trace summary structure in `state/kernel.py` for key loop events.
- Ensure summary updates are deterministic and side-effect-safe.
- Add/adjust targeted tests or smoke coverage proving event accounting is stable.
- Record validation evidence with `uv run python state/copilot_sdk_uv_smoke.py` mode(s) relevant to new trace summary checks.

## Expected files to touch
- `state/kernel.py`
- `state/copilot_sdk_uv_smoke.py`
- Targeted tests under `state/` (if present for touched helpers)
