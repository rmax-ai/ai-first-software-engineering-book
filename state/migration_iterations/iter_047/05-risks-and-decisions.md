# Risks and Decisions

## Risks discovered
- Live smoke validation depends on external Copilot service availability and credentials at run time.

## Decisions made and trade-offs
- Used `uv run` as the authoritative runtime for migration validation because `pyproject.toml` already declares `github-copilot-sdk` and live smoke succeeded there.
- Did not install into global/system Python to avoid environment-wide side effects in a shared workspace.

## Anything intentionally deferred
- None for this iteration.
