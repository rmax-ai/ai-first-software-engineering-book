# Risks and Decisions

## Risks discovered
- Kernel-level regression validation is currently blocked by ledger governance state (`hold`/`locked` on all chapters).

## Decisions made and trade-offs
- Did not modify `state/ledger.json` chapter statuses in this iteration to avoid policy-changing side effects.
- Treated this as a blocked iteration with explicit evidence rather than forcing non-minimal governance edits.

## Intentionally deferred
- Kernel-level mock regression with trace/resource assertions is deferred until one chapter is eligible.
