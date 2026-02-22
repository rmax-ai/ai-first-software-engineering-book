# Risks and decisions

## Risks discovered
- Planning without first implementation may miss hidden coupling in `state/kernel.py` and `state/role_io_templates.py`.
- Eval YAML changes can be brittle if new signals are introduced without stable deterministic fixtures.

## Decisions made
- Prioritized observability improvements first to make later behavioral regressions easier to detect.
- Kept this iteration strictly documentation/planning to satisfy seed-iteration requirements.

## Deferred intentionally
- Any direct code edits in `state/` or `evals/` are deferred to next iterations.
