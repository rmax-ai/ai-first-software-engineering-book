# Risks and decisions

## Risks discovered
- Planning artifacts can drift from real code if follow-up iterations skip targeted verification.
- Trace-summary and smoke coverage growth can create brittle checks unless mode guards stay minimal and explicit.

## Decisions made
- Chose a planning-only seed iteration per prompt contract.
- Scoped next iteration to one concrete implementation slice to reduce risk and keep diffs small.

## Deferred intentionally
- Any direct edits to `state/kernel.py`, `state/role_io_templates.py`, `state/copilot_sdk_uv_smoke.py`, or `evals/*.yaml`.
