# Next Iteration Recommendation

## Recommended next task
Unblock and execute the two remaining integration validations:
1) kernel-level mock regression on an eligible chapter, and
2) one live-provider smoke with reachable provider.

## Why it is next
All currently feasible migration tasks have been completed in this run; remaining unfinished coverage requires environment/governance prerequisites.

## Concrete acceptance criteria
- At least one chapter status is changed from `hold/locked` to eligible, then kernel mock run executes planner/writer/critic and produces `_llm_trace`.
- Configure `OPENAI_API_KEY` or start local Ollama, then one non-mock `LLMClient.chat(...)` call succeeds and records usage.

## Expected files to touch
- `state/ledger.json` (if governance status is unblocked)
- `state/migration_iterations/iter_013/*.md`
