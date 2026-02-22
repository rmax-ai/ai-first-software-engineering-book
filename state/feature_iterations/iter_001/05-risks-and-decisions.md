# Risks and decisions

## Risks discovered
- The planned harness changes touch core orchestration (`state/kernel.py`), so regressions in loop termination or evidence formatting are possible if implemented too broadly.
- Eval YAML changes can create false negatives if expected signals are not tightly aligned with harness outputs.

## Decisions made and trade-offs
- Chose a planning-only seed iteration to reduce implementation risk and establish explicit acceptance criteria before changing runtime behavior.
- Chose narrow, file-specific future slices instead of a multi-file implementation burst to keep diffs reviewable and verifiable.

## Intentionally deferred
- Any direct edits to `state/kernel.py`, `state/role_io_templates.py`, `state/copilot_sdk_uv_smoke.py`, or `evals/*.yaml`.
