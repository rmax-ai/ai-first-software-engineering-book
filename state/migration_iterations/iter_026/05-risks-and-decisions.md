# Risks and Decisions

## Risks discovered
- Existing fallback-specific smoke helper functions remain in file and are now unreachable via CLI mode dispatch.

## Decisions and trade-offs
- Kept changes minimal to complete one migration task; did not remove all legacy fallback helper code in this iteration.
- Prioritized behavior change and regression coverage over broader cleanup refactor.

## Intentionally deferred
- Full removal of obsolete HTTP fallback implementation/helpers from `state/llm_client.py` and `state/copilot_sdk_smoke_test.py`.
