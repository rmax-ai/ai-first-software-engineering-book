# Risks and decisions

## Risks
- Planned trace-schema additions in `state/kernel.py` may break consumers if output contracts are not versioned or tested.
- Tightening role I/O templates can surface latent prompt-shape assumptions in existing harness flows.
- Eval-rule updates may cause false negatives if thresholds are too strict before telemetry baselines are refreshed.

## Decisions and trade-offs
- Chose a planning-only iteration to establish implementation order and test/eval contracts before code edits.
- Chose minimal scope (artifact creation only) to avoid speculative harness modifications without explicit acceptance tests.

## Deferred items
- No code changes to kernel/templates/smoke/evals in this iteration; these are intentionally deferred to the next task.
