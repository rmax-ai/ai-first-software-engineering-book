# Recommended next task

## Task
Reduce mode documentation drift by deriving the module docstring usage/mode sections from shared mode metadata in `state/copilot_sdk_smoke_test.py`.

## Why it is next
- Runtime mode wiring is now table-driven, but user-facing mode documentation is still hand-maintained and can diverge.

## Acceptance criteria
1. Replace manually duplicated mode usage/mode description text with metadata-driven generation (or one centralized source) in `state/copilot_sdk_smoke_test.py`.
2. Keep CLI `--help` behavior and existing mode names unchanged.
3. Re-run at least `stub`, `bootstrap-failure`, and `trace-summary`.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_017/*`
