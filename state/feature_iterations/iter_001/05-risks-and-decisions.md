# Risks and decisions

## Risks discovered
- Planning-only output can become stale if implementation iterations drift from the declared sequence.
- Existing smoke matrix in `state/copilot_sdk_uv_smoke.py` is already dense; adding modes without factoring helpers may increase maintenance cost.
- Eval contract updates can create false negatives if metrics/trace expectations are not synchronized with kernel changes.

## Decisions made and trade-offs
- Decision: keep this iteration strictly planning-only to follow prompt seed constraints.
  - Trade-off: no immediate runtime behavior improvement yet.
- Decision: prioritize deterministic trace quality and role scaffold clarity before broader feature expansion.
  - Trade-off: some downstream ergonomics improvements are deferred.

## Intentionally deferred
- Any code edits to `state/kernel.py`, `state/role_io_templates.py`, `state/copilot_sdk_uv_smoke.py`, or `evals/*.yaml`.
