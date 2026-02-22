# Risks and Decisions

## Risks discovered
- Usage line assertions are order-sensitive; intentional mode ordering changes will require expected output updates.
- Guard currently checks canonical `--mode` lines only; format changes to prefixes could require adaptation.

## Decisions made
- Reused existing metadata-driven pattern (`_all_mode_specs`) to avoid duplicated mode lists.
- Scoped the guard to non-`stub` entries to match documented usage contract.

## Deferred intentionally
- No refactor of `_usage_doc_lines(...)` formatting behavior beyond deterministic coverage checking.
