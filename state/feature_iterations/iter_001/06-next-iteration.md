# Next Iteration Recommendation

## Recommended task (exactly one)
Implement deterministic trace summary enhancements in `state/kernel.py` and expose corresponding smoke assertions in `state/copilot_sdk_uv_smoke.py`.

## Why this is next
The plan identifies observability as the highest-leverage first implementation step and it unlocks measurable eval alignment in subsequent iterations.

## Acceptance criteria
- Add a minimal kernel trace summary signal that is deterministic and documented in code.
- Add/adjust smoke test coverage in `state/copilot_sdk_uv_smoke.py` that validates the new signal.
- Record verification evidence in `state/feature_iterations/iter_002/04-validation.md` using `uv run python state/copilot_sdk_uv_smoke.py`.

## Expected files to touch
- `state/kernel.py`
- `state/copilot_sdk_uv_smoke.py`
- `state/feature_iterations/iter_002/0{1..7}-*.md`
