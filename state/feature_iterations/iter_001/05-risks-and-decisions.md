# Risks and decisions

## Risks
- Plan granularity may still leave sequencing ambiguity when implementation starts.
- Existing eval schemas may require minor contract interpretation before adding new assertions.

## Decisions and trade-offs
- Chose a minimal, execution-ready backlog instead of speculative implementation details.
- Deferred exact test fixture payload shapes to the next iteration to keep this seed scope planning-only.

## Deferred items
- Concrete code edits in `state/kernel.py`, `state/role_io_templates.py`, `state/copilot_sdk_uv_smoke.py`, and `evals/*.yaml`.
