# Risks and decisions

## Risks discovered
- Long mode names remain error-prone for manual edits due repeated suffix chains.

## Decisions made and trade-offs
- Followed existing explicit-string style for consistency, despite verbosity.
- Kept scope to one runner + one mode registration to satisfy one-task iteration discipline.

## Intentionally deferred
- Any broader refactor to reduce duplicated long mode literals.
