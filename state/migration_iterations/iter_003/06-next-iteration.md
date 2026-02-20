# Next Iteration Recommendation

## Recommended next task
Harden SDK response handling in `state/llm_client.py` by aggregating `assistant.usage` event data when `session.send(...)` does not return dict usage directly.

## Why it is next
This iteration established guarded SDK routing; usage extraction hardening is the smallest follow-up needed to align with migration plan M1/M2 accounting requirements.

## Concrete acceptance criteria
- Usage extraction supports both direct response usage and event-stream usage shapes.
- Missing usage data safely falls back to zero without breaking `LLMUsage` schema.
- Existing mock/legacy HTTP paths remain unchanged.

## Expected files to touch
- `state/llm_client.py`
- `state/migration_iterations/iter_004/*.md`
