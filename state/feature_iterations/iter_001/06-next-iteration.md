# Next iteration recommendation

## Task
Add deterministic phase-trace validation and emission checkpoints in `state/kernel.py`.

## Why this is next
The plan's highest-leverage gap is reliable observability in the kernel loop; without stable phase traces, smoke/eval expansions will be less precise and harder to diagnose.

## Acceptance criteria
- `state/kernel.py` emits a structured phase trace payload at key loop stages (plan, execution, validation, completion).
- Phase trace payload shape is validated before write-out; malformed payloads fail loudly with actionable error text.
- Existing behavior remains intact for successful runs (no public CLI contract break).
- Targeted verification command(s) are documented and executed in the iteration artifacts.

## Expected files to touch
- `state/kernel.py`
- Optional helper tests under `state/` for phase trace validators
