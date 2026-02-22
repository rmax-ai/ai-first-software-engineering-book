# Risks and decisions

## Risks discovered
- Bulk replacement across many similarly named wrappers could accidentally alter unrelated assertions.

## Decisions made and trade-offs
- Used one exact multi-line assertion-block replacement pattern to keep the change mechanical and consistent.
- Preserved wrapper-local target mode names and PASS strings to avoid behavior drift.

## Deferred
- Wrapper definitions remain repetitive outside the shared assertion call; broader structural deduplication was deferred.
