# Risks and Decisions

## Risks discovered
- The next iteration may over-scope if feature, smoke, and eval updates are attempted together instead of one thin slice.
- Existing smoke/eval contracts may require tighter wording to avoid nondeterministic assertions.

## Decisions and trade-offs
- Kept this iteration planning-only to match the explicit seed requirement.
- Scoped the next task to one deterministic observability improvement plus targeted smoke/eval alignment.

## Deferred intentionally
- Any edits to `state/kernel.py`, `state/role_io_templates.py`, `state/copilot_sdk_uv_smoke.py`, or `evals/*.yaml` are deferred to future execution iterations.
