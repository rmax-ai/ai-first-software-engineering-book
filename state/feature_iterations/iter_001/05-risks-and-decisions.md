# Risks and Decisions

## Risks discovered
- Plan quality depends on accurate linkage between new kernel signals and eval assertions; poor mapping could produce false confidence.
- Future implementation may expand scope if role template updates and kernel logging are changed together without strict boundaries.

## Decisions and trade-offs
- Chose planning-only scope for this seed iteration to satisfy prompt intent and reduce risk of premature implementation.
- Deferred code edits until the next iteration to keep this change minimal and auditable.

## Deferred intentionally
- Any direct modifications to `state/kernel.py`, `state/role_io_templates.py`, `state/copilot_sdk_uv_smoke.py`, or `evals/*.yaml`.
