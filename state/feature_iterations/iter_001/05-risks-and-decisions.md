# Risks and decisions

## Risks
- Plan quality depends on current harness structure; if `state/kernel.py` changes before execution iterations, planned touch points may need small re-scoping.
- Eval wiring assumptions may drift if YAML contracts are revised independently.

## Decisions and trade-offs
- Chose planning-only output (no code edits) to match seed-iteration requirements exactly.
- Kept next task narrowly focused on trace schema and deterministic logging to enable incremental validation.

## Deferred intentionally
- Any implementation in `state/kernel.py`, template updates, or eval file changes.
- Smoke test additions until trace schema decisions are finalized.

