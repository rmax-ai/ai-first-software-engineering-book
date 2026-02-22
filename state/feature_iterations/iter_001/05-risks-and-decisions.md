# Risks and decisions

## Risks discovered
- Planning artifacts can drift from actual code constraints if future iterations skip re-validation against current `state/` behavior.
- Eval updates may become noisy without deterministic smoke signal definitions tied to explicit failure modes.

## Decisions made
- Keep this seed iteration planning-only, per prompt requirements.
- Prioritize deterministic trace/logging foundation before expanding eval contracts.
- Avoid speculative code changes until acceptance criteria are locked in the iteration backlog.

## Deferred intentionally
- No implementation in `state/kernel.py`, `state/role_io_templates.py`, `state/copilot_sdk_uv_smoke.py`, or `evals/*.yaml` in this iteration.
