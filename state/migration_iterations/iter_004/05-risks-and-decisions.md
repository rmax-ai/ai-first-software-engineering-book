# Risks and Decisions

## Risks discovered
- SDK event payload formats may vary beyond `type/event + usage/data` mappings.

## Decisions made and trade-offs
- Implemented conservative parsing that only consumes known token keys (`prompt_tokens/completion_tokens/input_tokens/output_tokens`).
- Limited scope to usage normalization only to avoid broad behavior changes during migration.

## Intentionally deferred
- Rich support for additional or nested SDK event schemas not currently observed in this repository.
