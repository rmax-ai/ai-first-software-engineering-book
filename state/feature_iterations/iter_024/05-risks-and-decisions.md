# Risks and Decisions

## Risks discovered
- Usage guard logic now exists across multiple focused modes; future edits must keep each mode’s assertion target distinct.

## Decisions made and trade-offs
- Added a dedicated set/count guard instead of broadening existing order or duplicate guards to keep failure diagnostics precise.
- Reused `_usage_doc_lines()` and `_all_mode_specs()` to avoid introducing another usage-generation path.

## Intentionally deferred
- No helper extraction for repeated usage-mode parsing in this iteration; scope limited to one smallest unfinished task.
