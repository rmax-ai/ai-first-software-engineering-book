# Risks and decisions

## Risks discovered
- The planned improvements span kernel orchestration and eval contracts, so sequencing mistakes could introduce noisy regressions.
- Existing harness behavior is only partially documented in iteration artifacts, increasing discovery cost for future implementers.

## Decisions and trade-offs
- Chose planning-only scope to keep this seed iteration minimal and aligned with prompt requirements.
- Deferred code edits so future iterations can validate one behavioral surface at a time with targeted smoke evidence.

## Deferred items
- Any direct edits to `state/kernel.py`, `state/role_io_templates.py`, `state/copilot_sdk_uv_smoke.py`, and `evals/*.yaml`.
