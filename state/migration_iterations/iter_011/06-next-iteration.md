# Next Iteration Recommendation

## Recommended next task
Attempt one live-provider smoke validation for SDK-backed path (`openai_compatible` or local `ollama`) and record explicit blocked evidence if credentials/runtime are unavailable.

## Why it is next
The migration plan still lists live-provider smoke as required coverage and this is the smallest remaining uncovered area.

## Concrete acceptance criteria
- Attempt one real provider run through `LLMClient.chat(...)` on non-mock provider.
- If successful, capture response/usage shape evidence.
- If blocked, capture exact blocking reason and minimal unblock action.

## Expected files to touch
- `state/migration_iterations/iter_012/*.md`
