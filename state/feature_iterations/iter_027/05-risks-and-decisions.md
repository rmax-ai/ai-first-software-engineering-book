# Risks and Decisions

## Risks discovered
- Duplicate diagnostics currently only include duplicated mode names; they do not include counts. This is acceptable for this scoped iteration but limits debugging detail.

## Decisions made and trade-offs
- Reused `_expected_non_stub_mode_names(...)` instead of introducing another helper to keep the diff minimal and align with prior consolidation work.
- Ordered duplicate reporting by expected mode registration order for deterministic output, rather than by first-seen runtime order.

## Intentionally deferred
- Enhancing duplicate diagnostics with per-mode duplicate counts.
