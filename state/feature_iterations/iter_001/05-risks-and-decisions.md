# Risks and decisions

## Risks discovered
- The plan assumes current eval contracts can absorb additional harness signals without schema drift.
- Smoke-test expansion may introduce longer runtime or flaky fixtures if deterministic setup is incomplete.

## Decisions and trade-offs
- Chose a planning-only iteration as required by the prompt seed guidance, deferring implementation to keep scope minimal and auditable.
- Kept the next-step recommendation to one narrow kernel-focused task to reduce integration risk.

## Intentionally deferred
- Any direct code edits in `state/kernel.py`, `state/role_io_templates.py`, `state/copilot_sdk_uv_smoke.py`, or `evals/*.yaml`.
