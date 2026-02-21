# Risks and Decisions

## Risks discovered
- The startup timeout cap (10s max) may be too strict on highly loaded environments.

## Decisions made and trade-offs
- Used bounded wait with explicit timeout/error messages to prioritize deterministic failure over indefinite blocking.
- Reused existing `_sdk_stage_error` mapping for consistency.

## Intentionally deferred
- No new dedicated bootstrap-failure smoke mode was added in this iteration.
