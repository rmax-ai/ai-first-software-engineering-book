# Risks and Decisions

## Risks discovered
- Remaining duplicate-count coverage-guard wrappers still use inlined logic, so inconsistent edits are still possible until the rollout completes.

## Decisions made and trade-offs
- Kept the established two-wrapper migration cadence to minimize verification scope and preserve deterministic iteration size.
- Limited edits to body delegation only; no function renames or mode table changes.

## Deferred intentionally
- Migration of the remaining higher-suffix wrappers was deferred to the next iteration to honor the one-task stop condition.
