# Plan

1. Add a deterministic smoke handler that inspects `__doc__` and asserts every mode name from `_all_mode_specs()` has a rendered `- <mode>:` entry.
2. Register the handler in shared mode metadata so it can be invoked via `--mode` without changing existing mode semantics.
3. Run required validation modes: `stub`, `bootstrap-failure`, and `trace-summary`; run the new mode as a focused guard check.
4. Record execution evidence and outcomes in iteration artifacts.

## Files expected to change
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_018/03-execution.md`
- `state/feature_iterations/iter_018/04-validation.md`
