# Risks and Decisions

## Risks discovered
- Repetitive wrappers are prone to drift if migration cadence breaks.
- Long mode strings remain fragile to manual editing errors.

## Decisions made and trade-offs
- Continued two-wrapper migration to keep diffs small and easy to validate.
- Deferred broader refactor (e.g., generated wrappers) to avoid changing established interfaces mid-rollout.

## Anything intentionally deferred
- Migrating remaining higher-suffix coverage-guard wrappers beyond this two-wrapper slice.
