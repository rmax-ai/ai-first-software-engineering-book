# Risks and decisions

## Risks discovered
- Planning quality depends on later iterations preserving small, testable slices.
- Harness behavior changes in `state/kernel.py` may affect deterministic outputs and eval stability.

## Decisions made
- Keep iter_001 documentation-only to satisfy seed prompt constraints.
- Prioritize first implementation work on observability hooks before broader refactors.

## Deferred intentionally
- Any direct edits to `state/kernel.py`, `state/role_io_templates.py`, smoke tests, or eval YAMLs.
