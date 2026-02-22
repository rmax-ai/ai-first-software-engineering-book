# Risks and Decisions

## Risks discovered
- Existing harness assumptions in `state/kernel.py` may couple logging, eval gating, and ledger writes more tightly than expected.
- Expanding smoke coverage can increase runtime and maintenance cost if scenarios are not deterministic.

## Decisions and trade-offs
- Chose planning-only iteration to avoid speculative code churn and establish testable acceptance criteria first.
- Kept backlog items small and file-scoped to support minimal diffs in follow-up iterations.

## Deferred intentionally
- No direct code edits to `state/kernel.py`, `state/role_io_templates.py`, `state/copilot_sdk_uv_smoke.py`, or `evals/*.yaml` in this iteration.
