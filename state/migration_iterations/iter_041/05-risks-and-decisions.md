# Risks and Decisions

## Risks discovered
- Smoke coverage relies on monkeypatching internals; refactors to shutdown internals could require test updates.

## Decisions made and trade-offs
- Chose a focused new mode rather than broad refactors to keep diff minimal and isolate one acceptance criterion.
- Retained existing mode names/output text to avoid downstream script breakage.

## Intentionally deferred
- No additional shutdown matrix expansion beyond the requested non-callable-destroy idempotency case.
