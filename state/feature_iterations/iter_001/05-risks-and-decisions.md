# Risks and decisions

## Risks discovered

- Planning-only iteration can drift from implementation reality if follow-up tasks are not kept narrow and validated each step.
- Kernel observability changes may increase output noise unless trace boundaries are explicit and test-gated.

## Decisions and trade-offs

- Chose a strict seed-planning scope (no code edits) to match the prompt contract exactly.
- Chose concrete file-level backlog items over speculative architecture changes to keep future tasks reviewable.

## Deferred intentionally

- Any implementation in `state/kernel.py`, `state/role_io_templates.py`, `state/copilot_sdk_uv_smoke.py`, or `evals/*.yaml`.
- Any metrics schema changes until a specific feature requires them.
