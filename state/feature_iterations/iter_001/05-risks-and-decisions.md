# Risks and decisions

## Risks
- Plan quality depends on later iterations preserving minimal-diff discipline while adding observability.
- Eval updates may drift if new kernel signals are added without synchronized YAML contract updates.

## Decisions and trade-offs
- Chose planning-only execution to match seed-iteration requirements, deferring implementation risk.
- Scoped next work to a single trace-summary observability slice to keep validation bounded.

## Deferred
- Direct edits to `state/kernel.py`, `state/role_io_templates.py`, `state/copilot_sdk_uv_smoke.py`, and eval YAMLs.
