# Risks and decisions

## Risks discovered

- Current harness behavior details may evolve quickly; backlog tasks must stay minimal to avoid drift between plan and implementation.
- Eval contract updates can be over-scoped if done before trace/role changes land, causing noisy iteration diffs.

## Decisions and trade-offs

- Chose a planning-only seed iteration per prompt requirement instead of making speculative code changes.
- Deferred implementation details to future single-task iterations to keep evidence and rollback boundaries clear.

## Deferred items

- Exact trace-summary schema changes in `state/kernel.py`.
- Exact smoke-mode names and assertions in `state/copilot_sdk_uv_smoke.py`.
- Specific threshold/wording changes in `evals/*.yaml`.
