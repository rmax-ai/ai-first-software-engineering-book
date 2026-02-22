# Risks and Decisions

## Risks discovered
- Kernel observability changes can increase log noise and make deterministic diffs harder if not schema-constrained.
- Expanding smoke coverage can create brittle checks unless assertions target stable signals.
- Eval contract tightening may surface latent drift in unrelated chapters.

## Decisions and trade-offs
- Chose a planning-only iteration to satisfy seed prompt constraints before implementation.
- Prioritized deterministic trace/accounting visibility first because it improves debuggability for all later harness changes.
- Deferred implementation details to keep this iteration minimal and reviewable.

## Intentionally deferred
- Direct code edits in `state/kernel.py`, `state/role_io_templates.py`, `state/copilot_sdk_uv_smoke.py`, and `evals/*.yaml`.
