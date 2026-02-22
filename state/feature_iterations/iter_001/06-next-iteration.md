# Next Iteration Recommendation

## Recommended next task
Implement deterministic kernel trace logging and expose it in iteration evidence.

## Why this is next
- It is the smallest vertical slice that improves observability while preserving current interfaces.
- It unlocks safer follow-on work in templates, smoke tests, and eval gates by providing concrete trace signals.

## Acceptance criteria
1. `state/kernel.py` emits structured trace entries for major loop phases and failure exits.
2. Trace output can be observed in a targeted harness run (documented command + output excerpt).
3. `state/copilot_sdk_uv_smoke.py` includes at least one check that confirms trace signal presence.
4. Iteration artifacts document verification steps and pass/fail evidence.

## Expected files to touch
- `state/kernel.py`
- `state/copilot_sdk_uv_smoke.py`
- `state/feature_iterations/iter_002/03-execution.md`
- `state/feature_iterations/iter_002/04-validation.md`
