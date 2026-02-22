# Risks and decisions

## Risks discovered
- The smoke file has many near-duplicate guard functions; broad scripted edits could unintentionally affect non-targeted modes.

## Decisions made and trade-offs
- Used a targeted regex scoped to `run_usage_examples_duplicate_count_mode_coverage_guard*` function signatures to keep diff focused.
- Left unrelated `mode_action = next(...)` call sites untouched.

## Deferred
- Broader deduplication of repeated guard functions remains deferred to keep this iteration scoped to one backlog task.
