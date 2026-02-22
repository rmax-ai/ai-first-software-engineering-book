# Risks and decisions

## Risks discovered
- Each deterministic mode shells out to `uv run`, so runtime cost increases and failures can include environment-level issues unrelated to assertion logic.
- Output matching depends on known smoke message fragments; future message wording changes may require test updates.

## Decisions and trade-offs
- Chose end-to-end subprocess assertions over local fixture-only assertions to validate the real fixture-backed kernel path used in `state/copilot_sdk_uv_smoke.py`.
- Enforced strict `state/ledger.json` immutability checks in deterministic smoke modes to guard against repository-state side effects.

## Deferred
- Consolidating repetitive usage-example duplicate-count guard modes remains deferred because it is unrelated to this iteration’s scoped acceptance criteria.
