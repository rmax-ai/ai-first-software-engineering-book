# Risks and Decisions

## Risks discovered
- No new regressions were observed in deterministic non-live smoke coverage after adding the new mode.

## Decisions made and trade-offs
- Reused the existing shutdown-mode helper and assertion style to keep behavior consistent and diff size minimal.
- Ran the full deterministic non-live matrix in addition to the targeted mode to reduce risk of incidental breakage.

## Deferred items
- Live-provider smoke remains deferred; this iteration intentionally focused on deterministic shutdown hardening.
