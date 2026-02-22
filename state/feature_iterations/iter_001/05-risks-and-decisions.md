# Risks and Decisions

## Risks
- Backlog items may be too broad if next iterations do not keep changes narrowly scoped.
- New observability hooks in `state/kernel.py` could add noisy output unless explicitly gated.

## Decisions and trade-offs
- Decision: keep this iteration planning-only to minimize risk and establish a clear backlog first.
- Trade-off: no immediate harness behavior improvements this iteration, but lower execution risk in follow-up implementation tasks.

## Deferred intentionally
- Actual code changes in `state/kernel.py`, `state/role_io_templates.py`, and `state/copilot_sdk_uv_smoke.py` deferred to next iteration.
