# Risks and decisions

## Risks discovered
- Planning-only iterations can drift if next-task acceptance criteria are vague.
- Trace logging additions in `state/kernel.py` could increase noise unless output schemas are kept deterministic.
- Expanding smoke coverage may increase runtime unless modes remain targeted.

## Decisions and trade-offs
- Chose a planning-first iteration per prompt seed requirement; no harness code changes were made.
- Prioritized explicit file-level mapping so future iterations can execute with minimal ambiguity.
- Deferred implementation details (exact trace schema fields, smoke mode naming) to the next task to keep this iteration minimal.

## Intentionally deferred
- Any edits to `state/kernel.py`, `state/role_io_templates.py`, `state/copilot_sdk_uv_smoke.py`, or `evals/*.yaml`.
- Any test/eval runtime execution beyond validating the planning artifact contract.
