# Next iteration recommendation

## Task
Implement deterministic trace logging checkpoints in `state/kernel.py`.

## Why next
- The seed plan identifies observability as the foundational dependency for safely evolving role templates, smoke scenarios, and eval gates.
- Adding deterministic trace checkpoints first gives immediate evidence for subsequent iterations and reduces regression triage time.

## Acceptance criteria
- Add explicit trace checkpoints at major kernel phases (plan/build/validate/emit) with stable field naming.
- Ensure checkpoints are emitted through existing harness output paths without changing public CLI behavior.
- Add/adjust targeted smoke coverage in `state/copilot_sdk_uv_smoke.py` proving checkpoints appear in successful and failing flows.
- Record expected verification command(s) and outcomes in the next iteration’s `04-validation.md`.

## Expected files to touch
- `state/kernel.py`
- `state/copilot_sdk_uv_smoke.py`
