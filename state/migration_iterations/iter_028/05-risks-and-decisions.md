# Risks and Decisions

## Risks discovered
- Background loop startup currently waits indefinitely for readiness if thread boot fails unexpectedly.

## Decisions made and trade-offs
- Chose a persistent worker loop for nested-loop contexts to avoid unsafe ad-hoc event loops.
- Kept main-thread reusable loop behavior unchanged for non-running-loop contexts to minimize migration scope.

## Anything intentionally deferred
- No additional timeout/error-mapping hardening was added for worker-loop bootstrap in this iteration.
