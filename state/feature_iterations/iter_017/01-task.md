# Task: Derive smoke mode docs from shared metadata

## Why this task now
- `state/feature_iterations/iter_016/06-next-iteration.md` identified drift risk between hand-written module docs and table-driven mode wiring.
- Completing this now keeps user-facing mode documentation aligned with runtime mode registration.

## Acceptance criteria
1. Replace duplicated top-of-file usage/mode content in `state/copilot_sdk_smoke_test.py` with metadata-driven generation from existing mode tables.
2. Keep mode names and CLI `--help` behavior unchanged.
3. Re-run `stub`, `bootstrap-failure`, and `trace-summary`.
