# Risks and Decisions

## Risks discovered
- Current check validates status context but does not assert response-body detail text.

## Decisions made and trade-offs
- Kept assertion focused on status code context (`HTTP fallback failed (500)`) for stable actionable mapping.
- Continued using deterministic local server and monkeypatch to avoid external dependencies.

## Intentionally deferred
- Additional fallback error regressions for invalid JSON and URL/network failure branches.
