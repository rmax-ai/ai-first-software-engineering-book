# Risks and Decisions

## Risks discovered
- Duplicate counts now improve diagnostics, but the guard still only reports duplicates and not missing modes; that coverage remains split across other usage-example guard modes.

## Decisions made and trade-offs
- Used a deterministic dictionary comprehension keyed by `_expected_non_stub_mode_names(...)` to keep output stable across runs.
- Kept message formatting simple (`{mode: count}`) to minimize diff size and preserve existing guard behavior.

## Intentionally deferred
- Consolidating usage-example guard diagnostics across coverage/order/set guards into a shared formatter helper.
