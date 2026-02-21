# Validation

## Verification commands run
1. `uv run python state/copilot_sdk_smoke_test.py --mode stub`
2. `uv run python state/copilot_sdk_smoke_test.py --mode sdk-unavailable`
3. `uv run python - <<'PY' ... asyncio.run(main()) ... PY`

## Observed outputs/results
- Stub mode: `PASS: stub Copilot SDK path works`.
- SDK-unavailable mode: `PASS: copilot provider requires SDK when module is unavailable`.
- Nested-loop check: `PASS: nested loop sync bridge works`.

## Pass/fail against acceptance criteria
- Running-loop handling avoids ad-hoc same-thread loop execution: **PASS**.
- `chat(...)` interface unchanged: **PASS**.
- Required smoke modes pass: **PASS**.
