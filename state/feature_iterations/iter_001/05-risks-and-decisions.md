# Risks and Decisions

## Risks
- Plan scope may still be broad if next iteration attempts multiple harness features at once.
- Eval coupling risk: changes in `state/kernel.py` can affect multiple YAML gates simultaneously.

## Decisions and trade-offs
- Chose a planning-only iteration to match the seed prompt exactly.
- Deferred implementation details to keep this iteration minimal and reviewable.

## Deferred intentionally
- No edits to harness/runtime files in `state/` beyond iteration artifacts.
- No eval YAML or smoke-script code changes in this iteration.
