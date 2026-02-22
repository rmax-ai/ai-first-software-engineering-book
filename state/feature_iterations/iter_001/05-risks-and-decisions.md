# Risks and decisions

## Risks discovered
- The plan depends on preserving deterministic kernel behavior while adding richer observability; uncontrolled schema changes in metrics could break downstream tooling.
- New smoke modes may increase maintenance burden unless they stay table-driven and reuse existing mode dispatch patterns.

## Decisions and trade-offs
- Chose a planning-only iteration to satisfy seed requirements and minimize implementation risk.
- Reused existing eval contracts (`evals/*.yaml`) as regression anchors instead of proposing new eval files in this step.

## Deferred intentionally
- Direct edits to `state/kernel.py`, `state/role_io_templates.py`, and `state/copilot_sdk_uv_smoke.py` are deferred to the next iteration.
