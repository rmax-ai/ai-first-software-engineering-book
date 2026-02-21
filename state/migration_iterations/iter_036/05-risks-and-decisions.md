# Risks and Decisions

## Risks discovered
- The idempotency assertion currently covers the stop/force_stop failure branch and may not catch regressions isolated to destroy-only failures.

## Decisions made and trade-offs
- Reused the existing shutdown-failure setup pattern to keep the change minimal and deterministic.
- Asserted full first-failure message details before second `close()` to ensure idempotency coverage does not weaken existing failure expectations.

## Intentionally deferred
- Separate idempotency coverage for destroy-failure branch remains deferred to keep this iteration to one smallest task.
