# Risks and Decisions

## Risks
- Trace schema expansion in `state/kernel.py` can create compatibility drift with existing smoke expectations if not phased.
- Tightening role template contracts may expose undocumented assumptions in current prompts.
- Eval contract updates may fail if acceptance signals are not mapped to deterministic metrics.

## Decisions and trade-offs
- Chose a planning-only iteration to reduce implementation risk and preserve current runtime behavior.
- Prioritized deterministic observability and verification pathways before feature coding.
- Deferred implementation details until each item can be executed as a smallest single-task iteration.

## Deferred items
- Actual kernel/template/smoke/eval code changes.
- New or updated tests tied to those implementation changes.
