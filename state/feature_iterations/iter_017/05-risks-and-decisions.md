# Risks and decisions

## Risks discovered
- Module docstring is generated at import time, so future mode table edits must keep descriptions concise for readability.

## Decisions and trade-offs
- Reused existing mode tables and added lightweight helper functions instead of introducing new data structures.
- Kept generated usage output format compatible with existing command examples (`uv run python ...`).

## Deferred items
- Add a focused unit/assertion test that checks generated module docs include all registered mode names.
