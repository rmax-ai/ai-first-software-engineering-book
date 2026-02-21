# Risks and Decisions

## Risks discovered
- SDK failure shapes can vary by provider/runtime, so message detail extraction remains best-effort from exception text.

## Decisions made and trade-offs
- Added stage-specific wrapping close to each lifecycle await/call rather than broad classification after-the-fact.
- Kept existing broad fallback `Copilot SDK chat failed` for unexpected uncategorized exceptions.

## Intentionally deferred
- Structured exception-class-specific mapping (e.g., auth vs transport classes) deferred to keep this iteration minimal and single-task.
