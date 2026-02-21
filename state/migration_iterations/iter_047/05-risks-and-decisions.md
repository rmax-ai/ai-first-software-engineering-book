# Risks and Decisions

## Risks discovered
- System Python (`python`) still does not import `copilot` in this environment; only the project-managed runtime succeeds.

## Decisions made and trade-offs
- Used `uv run` as the authoritative runtime for migration validation because `pyproject.toml` already declares `github-copilot-sdk` and live smoke succeeded there.
- Did not install into global/system Python to avoid environment-wide side effects in a shared workspace.

## Anything intentionally deferred
- Aligning documentation and validation command examples so they consistently use `uv run` instead of bare `python`.
