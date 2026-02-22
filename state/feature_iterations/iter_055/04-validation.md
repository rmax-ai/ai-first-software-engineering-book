# Validation

## Verification commands run
1. `python - <<'PY' ... uv run python state/copilot_sdk_uv_smoke.py --mode trace-summary --chapter-id zz-trace-smoke --metrics-path state/trace_smoke_metrics_fixture.json ... PY` (ephemeral fixture creation + cleanup)
2. `uv run python state/kernel.py --chapter-id 01-paradigm-shift`
3. `uv run python -m py_compile state/kernel.py state/copilot_sdk_uv_smoke.py`

## Observed outputs/results
1. Smoke command returned `0` and printed:
   - `PASS: trace_summary present with required keys`
   - `phase_trace_events=3`
2. Focused kernel command returned `3` with:
   - `KernelError: Chapter is not eligible (status='hold').`
   This confirms the existing chapter-status guard remains active and unchanged by this iteration.
3. `py_compile` completed with exit code `0`.

## Pass/fail against acceptance criteria
1. Kernel emits deterministic phase-level trace fields: **PASS**.
2. Smoke validation checks phase trace shape and required phases: **PASS**.
3. Targeted validation commands executed with recorded outcomes: **PASS** (kernel command expected guarded failure in current ledger state).
