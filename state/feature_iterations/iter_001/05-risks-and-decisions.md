# Risks and decisions

## Risks discovered
- Planning quality may drift from actual harness constraints if future iterations skip command-backed verification.
- Eval updates can accidentally widen scope if not tied to specific harness behaviors.

## Decisions and trade-offs
- Chose planning-only output for this seed iteration to establish a clean backlog before code edits.
- Prioritized deterministic, test-first follow-up work over speculative refactors.

## Intentionally deferred
- Direct implementation in `state/kernel.py`, `state/role_io_templates.py`, and `state/copilot_sdk_uv_smoke.py`.
- Eval YAML edits until the first concrete behavior change is selected.
