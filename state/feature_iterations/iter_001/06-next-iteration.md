# Recommended next iteration

## Next task
Implement deterministic trace-summary hardening in `state/kernel.py` and prove it through smoke coverage updates.

## Why this is next
Trace-summary consistency is the foundation for validating future harness behavior, and it provides immediate observability benefits for every subsequent task in this backlog.

## Acceptance criteria
- Add/adjust kernel helper logic so trace summaries always emit stable required fields.
- Extend `state/copilot_sdk_uv_smoke.py` with at least one deterministic mode that fails if trace-summary shape regresses.
- Update validation notes to reference the exact smoke command and expected pass signal.

## Expected files to touch
- `state/kernel.py`
- `state/copilot_sdk_uv_smoke.py`
- `state/feature_iterations/iter_002/03-execution.md`
- `state/feature_iterations/iter_002/04-validation.md`
