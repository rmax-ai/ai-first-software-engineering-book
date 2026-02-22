# Risks and decisions

## Risks discovered
- Expanding trace logging may increase output noise or break downstream parsers if schemas are not versioned.
- Smoke assertions can become brittle if tied to unstable message text instead of structured fields.

## Decisions and trade-offs
- Prioritize structured, additive trace fields in `state/kernel.py` over free-form log text.
- Keep initial implementation scope narrow (kernel trace summary + smoke assertions) before touching eval YAMLs.

## Deferred items
- Eval contract updates are deferred until concrete kernel outputs change and can be validated with evidence.
