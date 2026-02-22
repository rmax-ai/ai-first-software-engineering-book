# Risks and decisions

## Risks discovered
- Source-text regression checks can miss semantic regressions that do not include `_all_mode_specs()` literal text.
- Additional duplicate-count wrappers in future may need this guard logic updated if naming patterns change.

## Decisions and trade-offs
- Used `inspect.getsource(...)` for deterministic, low-overhead wrapper-body validation.
- Scoped the guard to mode handlers registered in `TRACE_SUMMARY_MODE_SPECS` to avoid broad unrelated introspection.

## Deferred intentionally
- Broader AST-level wrapper-shape validation was deferred to keep this iteration minimal.
