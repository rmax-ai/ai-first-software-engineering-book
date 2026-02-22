# Risks and decisions

## Risks discovered
- Fixture-only assertions do not validate live metrics file structure changes outside smoke fixtures.

## Decisions and trade-offs
- Used deterministic inline fixtures to avoid flaky dependencies on kernel execution or local metrics state.
- Added shared helper checks so both positive and negative cases verify the same required-key contract.

## Deferred intentionally
- Cross-tool reuse of trace-summary validation helpers between `copilot_sdk_smoke_test.py` and `copilot_sdk_uv_smoke.py`.

## Loop self-evaluation
- **Goal check:** Completed the requested next task from `iter_004` by adding one success path and one missing-key path in the deterministic smoke matrix.
- **Evidence check:** Verified with `py_compile` and direct execution of both new modes; both passed.
- **Risk check:** Coverage is deterministic and schema-focused, but does not run kernel-generated metrics in this test file.
- **Next-step decision:** Stop this iteration and hand off one bounded follow-up task for broader integration coverage.
