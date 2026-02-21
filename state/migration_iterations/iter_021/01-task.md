# Task

## Selected task title
Add deterministic regression coverage for HTTP fallback invalid JSON handling in `state/copilot_sdk_smoke_test.py`.

## Why this task now
`state/migration_iterations/iter_020/06-next-iteration.md` identified invalid JSON parsing in fallback mode as the next uncovered high-risk branch.

## Acceptance criteria
- Add a smoke mode that forces fallback path and returns a non-JSON payload.
- Assert `LLMClientError` includes `HTTP fallback returned invalid JSON` context.
- Mode fails non-zero on regression.
