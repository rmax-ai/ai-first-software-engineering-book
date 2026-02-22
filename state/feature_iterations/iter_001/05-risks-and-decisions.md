# Risks and Decisions

## Decisions
- Kept this iteration strictly planning-focused to match seed constraints.
- Prioritized kernel observability as the first implementation candidate because it offers high debugging value with localized code impact.

## Risks
- Backlog sequencing may need adjustment once concrete kernel internals are inspected during implementation.
- Some eval YAML edits may be unnecessary if existing gates already cover the chosen feature; verify before changing eval files.

## Deferred items
- Direct edits to `state/kernel.py`, `state/role_io_templates.py`, and smoke tests are intentionally deferred to the next implementation iteration.
