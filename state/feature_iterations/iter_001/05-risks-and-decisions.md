# Risks and Decisions

## Risks discovered
- Future iterations may over-scope changes across kernel, templates, smoke matrix, and eval contracts if not split into small deltas.
- Trace logging additions in `state/kernel.py` can create noisy outputs unless logging schema is explicitly constrained.

## Decisions and trade-offs
- Chose planning-only execution for this seed iteration to satisfy prompt requirements and avoid premature implementation.
- Captured one integrated backlog that maps behaviors to tests/evals, trading immediate code delivery for clearer execution sequencing.

## Deferred intentionally
- No code changes to harness modules in this iteration.
- No eval YAML edits until a concrete feature delta is selected in the next iteration.
