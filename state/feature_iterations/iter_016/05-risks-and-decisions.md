# Risks and decisions

## Risks discovered
- The top-of-file usage and mode documentation remains manually maintained, so text can still drift from runtime mode tables.

## Decisions and trade-offs
- Scoped this iteration to base mode table-driving only, matching the prior handoff and minimizing behavior risk.
- Reused existing shutdown/trace-summary tables instead of introducing a new abstraction layer.

## Deferred items
- Optionally derive top-of-file usage and mode docs from shared mode metadata to remove remaining duplication.
