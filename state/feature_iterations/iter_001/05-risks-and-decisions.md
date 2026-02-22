# Risks and Decisions

## Risks discovered
- Planning quality risk: future implementation could drift without strict acceptance criteria tied to deterministic smoke outputs.
- Coupling risk: logging changes in `state/kernel.py` may affect eval assumptions if trace formats are unstable.

## Decisions made
- Keep this iteration planning-only per seed prompt to avoid premature code churn.
- Require each future implementation step to include explicit smoke/eval evidence and measurable expected signals.

## Deferred intentionally
- No direct code edits to harness modules in this iteration.
- No eval YAML edits until the first concrete behavior change is implemented.
