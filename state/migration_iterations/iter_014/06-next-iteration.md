# Next Iteration Recommendation

## Recommended next task
No remaining in-repo migration task is unfinished. Only external-prerequisite checks remain (live-provider availability).

## Why it is next
Migration acceptance coverage is complete for feasible in-repo tasks; additional progress requires environment setup outside repository code.

## Concrete acceptance criteria
- `OPENAI_API_KEY` is configured or local Ollama runtime is reachable.
- Run one non-mock `LLMClient.chat(...)` smoke and capture usage evidence.
- Write `iter_015` artifacts only if those prerequisites are newly available.

## Expected files to touch
- `state/migration_iterations/iter_015/*.md` (only if prerequisites are available)
