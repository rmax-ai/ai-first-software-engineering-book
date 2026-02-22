# Risks and decisions

## Risks discovered
- Planning artifacts can drift from actual harness state if follow-up iterations defer implementation too long.
- Observability additions in `state/kernel.py` may increase output volume if not bounded.
- Eval wiring can become brittle if YAML contracts and smoke outputs are changed independently.

## Decisions made
- Prioritized a planning-only iteration to reduce implementation churn and force explicit acceptance criteria first.
- Chose deterministic, file-specific backlog items over broad refactor themes.
- Anchored future verification to existing uv smoke and eval contracts to detect regressions early.

## Deferred intentionally
- No runtime behavior changes in `state/` were implemented in this iteration.
- No eval YAML modifications were made before a concrete implementation task is selected.
