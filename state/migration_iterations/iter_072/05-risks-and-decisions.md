# Risks and Decisions

## Risks discovered
- Shell backticks in search patterns can trigger command substitution if not escaped, so literal `rg -nF` usage is required for reliable validation.

## Decisions made and trade-offs
- Executed only the one-line handoff task to keep scope minimal and deterministic.
- Committed the file edit immediately (`b3a2d1b`) to satisfy auto-commit expectations.

## Intentionally deferred
- Additional historical artifact normalizations were deferred to the next iteration by design.
