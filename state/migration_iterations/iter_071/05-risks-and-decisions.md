# Risks and Decisions

## Risks discovered
- Pattern searches for `python ...` can overlap with normalized `uv run python ...` text, so validation interpretation must explicitly check for bare snippet absence.

## Decisions made and trade-offs
- Per prior handoff, executed the smallest possible one-line artifact edit and avoided unrelated cleanup.
- Committed the line edit immediately (`35a203f`) to satisfy requested auto-commit behavior on meaningful change batches.

## Intentionally deferred
- Adjacent historical normalization steps outside the selected one-line scope were deferred to the next iteration.
