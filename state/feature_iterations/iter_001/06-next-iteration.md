# Recommended next task

## Task
Implement deterministic trace checkpoint helpers in `state/kernel.py` and cover them with targeted smoke assertions in `state/copilot_sdk_uv_smoke.py`.

## Why this is next
- It establishes the observability foundation needed before role-IO schema tightening and eval-gate expansion.

## Acceptance criteria
- Add checkpoint helper(s) in `state/kernel.py` that emit stable, testable trace summary entries.
- Extend `state/copilot_sdk_uv_smoke.py` with at least one deterministic mode validating the new checkpoint entry shape.
- Run `uv run python state/copilot_sdk_uv_smoke.py --mode <new-mode>` and record passing output in the next iteration validation artifact.

## Expected files to touch
- `state/kernel.py`
- `state/copilot_sdk_uv_smoke.py`

