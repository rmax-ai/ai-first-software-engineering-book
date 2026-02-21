# Risks and Decisions

## Risks discovered
- Low risk: this was a documentation-only one-line normalization in historical iteration artifacts.

## Decisions made and trade-offs
- Chose the smallest possible diff (single line) to preserve prior artifact context while normalizing command wording.
- Kept validation focused on literal `rg` matching and scoped git diff evidence only.

## Anything intentionally deferred
- Deferred broader historical wording sweeps; only the explicitly handed-off snippet mention was changed.
