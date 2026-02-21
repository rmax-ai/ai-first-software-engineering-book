# Risks and Decisions

## Risks discovered
- The fallback regression validates one OpenAI-compatible fallback shape only.

## Decisions made and trade-offs
- Kept assertions narrow and deterministic to minimize flakiness.
- Used temporary monkeypatching of `importlib.import_module` to force fallback without external environment setup.

## Intentionally deferred
- Additional fallback error-shape regression cases (HTTP error/invalid JSON paths).
