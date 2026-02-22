# Risks and decisions

## Risks
1. `state/kernel.py` changes can easily introduce nondeterministic behavior unless guard checks remain table-driven and reproducible.
2. Role template tightening in `state/role_io_templates.py` may break existing prompt assumptions if migration coverage is incomplete.
3. Expanding smoke modes without stable assertions can create brittle tests.

## Decisions and trade-offs
- Decided to keep this iteration planning-only to de-risk implementation sequencing.
- Deferred code edits until feature slices can be validated with targeted smoke and eval checks.
- Chose eval-first mapping so each future change is tied to explicit regression signals.

## Intentionally deferred
- No Python implementation changes in this iteration.
- No eval YAML edits in this iteration; only mapping and planning were documented.
