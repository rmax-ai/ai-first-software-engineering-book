# Next iteration

## Recommended next task
Add deterministic cleanup assertions in `state/copilot_sdk_smoke_test.py` to verify fixture directories under `state/.smoke_fixtures/trace_summary/` are removed after each kernel-backed smoke mode.

## Why it is next
Kernel-backed mode coverage is now deterministic and ledger-safe; the next stability guard is explicit fixture-cleanup verification to prevent state leakage across smoke runs.

## Concrete acceptance criteria
1. Add one deterministic mode that runs all kernel-backed trace-summary variants and asserts fixture roots are absent after each run.
2. Keep assertions repository-safe by confirming `state/ledger.json` remains unchanged.
3. Record command output and pass/fail evidence in `state/feature_iterations/iter_064/04-validation.md`.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_064/*.md`
