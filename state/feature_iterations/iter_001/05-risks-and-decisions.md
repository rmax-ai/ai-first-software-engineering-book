# Risks and decisions

## Risks discovered
- Planning without immediate implementation can leave ambiguity around required refactors in `state/kernel.py`.
- Expanding smoke coverage may increase runtime and maintenance cost if mode permutations grow unchecked.

## Decisions made and trade-offs
- Chose a planning-only iteration to follow the seed prompt exactly; deferred code edits to later iterations.
- Scoped backlog to deterministic, testable harness changes rather than broad architecture rewrite to keep subsequent diffs minimal.

## Intentionally deferred
- Concrete code changes in `state/kernel.py`, `state/role_io_templates.py`, and `state/copilot_sdk_uv_smoke.py`.
- Any eval YAML edits pending first implementation step and observed behavior deltas.
