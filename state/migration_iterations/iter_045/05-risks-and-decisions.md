# Risks and Decisions

## Risks discovered
- No deterministic regressions were observed after adding the new shutdown-mode branch.

## Decisions made and trade-offs
- Reused existing shutdown-mode helpers and assertion style to keep the diff minimal and consistent.
- Kept validation deterministic-only; live-provider checks remain intentionally deferred.

## Deferred items
- A live-provider smoke pass is still pending to validate end-to-end behavior outside deterministic stubs.
