# Task

## Selected task title
Add deterministic regression coverage for HTTP fallback non-object payload mapping in `state/copilot_sdk_smoke_test.py`.

## Why this task now
`iter_024/06-next-iteration.md` explicitly called out this missing fallback mapping case, and all other fallback mapping cases were already covered.

## Acceptance criteria
- Add a new smoke-test mode that forces HTTP fallback and returns JSON that is not an object.
- Assert the raised error message contains `HTTP fallback returned non-object payload`.
- Mode exits non-zero if the mapping regresses.
