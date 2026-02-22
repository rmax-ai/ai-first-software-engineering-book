# Risks and Decisions

## Risks discovered

- Plan quality risk: future implementation may drift if feature/test/eval linkage is not kept explicit per task.
- Regression visibility risk: adding diagnostics without updating eval gates can create false confidence.

## Decisions and trade-offs

- Chose planning-only execution to satisfy the seed-iteration contract exactly.
- Chose concise backlog slices over detailed pseudo-code to keep next iterations flexible and minimal-diff.

## Intentionally deferred

- Any direct edits to `state/kernel.py`, `state/role_io_templates.py`, `state/copilot_sdk_uv_smoke.py`, or `evals/*.yaml`.
- Running harness smoke/unit tests, since no executable code changes were made in this iteration.
