# Risks and Decisions

## Risks discovered
- Direct live-provider behavior was not exercised in this iteration; validation is focused to shutdown semantics.

## Decisions made and trade-offs
- Kept diff minimal: only reference-reset points on successful `stop()`/`force_stop()` completion.
- Preserved existing error-raising behavior when `session.destroy()` fails, even if client stop succeeds.

## Intentionally deferred
- End-to-end kernel-level live-provider smoke validation remains deferred to a dedicated iteration.
