# Risks and Decisions

## Risks discovered
- Additional high-suffix wrappers still contain duplicated inline logic and remain susceptible to future drift until rollout completion.

## Decisions made and trade-offs
- Continued the two-wrapper migration cadence to keep each iteration tightly scoped and easy to validate.
- Limited edits to wrapper delegation only; no mode registration changes were made.

## Deferred intentionally
- Migration of remaining duplicate-count wrappers beyond this pair was deferred to the next iteration.
