# Risks and Decisions

## Risks discovered
- Kernel does not yet call `close()` in a `finally` block, so cleanup is still best-effort.

## Decisions and trade-offs
- Implemented only a no-op compatibility hook now to keep this iteration minimal and low-risk.
- Deferred kernel control-flow edits to a dedicated follow-up iteration.

## Intentionally deferred
- `state/kernel.py` teardown wiring (`finally` + `client.close()` / `client.stop()` fallback).

