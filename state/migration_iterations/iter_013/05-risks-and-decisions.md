# Risks and Decisions

## Risks discovered
- Mock-provider writer output currently violates heading-preservation guard, blocking kernel completion in LLM mode.
- File-driven fallback remains blocked when role output triplet is absent.

## Decisions made and trade-offs
- Decision: treat this iteration as blocked with full evidence rather than broad code changes.
- Trade-off: no behavioral fix landed in this iteration; preserves migration diff discipline.

## Anything intentionally deferred
- Any change to mock writer generation behavior in `state/llm_client.py`.
- Manual authoring of file-driven role outputs for `iter_03`.
