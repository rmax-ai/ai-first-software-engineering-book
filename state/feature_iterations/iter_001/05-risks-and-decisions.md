# Risks and Decisions

## Risks discovered
- Without richer kernel traces, future regressions may be hard to diagnose from iteration artifacts alone.
- Updating eval contracts too early could create brittle gates before observability signals are stabilized.

## Decisions and trade-offs
- Chose planning-only scope per seed iteration contract instead of touching runtime code now.
- Kept backlog focused on one vertical slice for the next iteration to reduce risk and simplify verification.

## Intentionally deferred
- No code edits to `state/kernel.py`, `state/role_io_templates.py`, `state/copilot_sdk_uv_smoke.py`, or `evals/*.yaml` in this iteration.
- Detailed schema/format for new trace logs is deferred to the next implementation task.
