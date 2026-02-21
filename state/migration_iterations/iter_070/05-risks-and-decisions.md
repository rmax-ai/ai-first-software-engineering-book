# Risks and Decisions

## Risks discovered
- Search strings that include `python ...` also match normalized `uv run python ...`, so validation interpretation must remain explicit.

## Decisions made and trade-offs
- Chose a one-line text-only edit in the historical artifact to keep scope minimal and aligned with prior-iteration guidance.
- Committed the task edit immediately (`eb71328`) to satisfy auto-commit behavior for meaningful change batches.

## Intentionally deferred
- Remaining normalization work in adjacent historical files (for fallback-timeout wording) was deferred to the next iteration.
