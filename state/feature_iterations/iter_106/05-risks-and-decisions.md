# Risks and decisions

## Risks discovered
- The new guard checks ordering for this specific pair only; additional ordering constraints between other helper hardening guards remain unprotected.

## Decisions made and trade-offs
- Reused existing `TRACE_SUMMARY_MODE_SPECS` index-based guard style for deterministic behavior and minimal diff scope.
- Limited verification to the requested mode to keep iteration scope to one backlog task.

## Anything intentionally deferred
- Broader ordering constraints across more duplicate-count helper hardening modes were deferred.
