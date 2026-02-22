# Summary

Completed one focused backlog task from `iter_005` by adding malformed `trace_summary` type-shape regression coverage.
Implemented deterministic `trace-summary-shape-guard` mode in `state/copilot_sdk_smoke_test.py`.
Wired the new mode into usage docs, CLI mode choices, and dispatcher flow.
Used the existing `_get_latest_trace_summary` assertion contract to keep validation behavior consistent.
Ran targeted compile and smoke mode verification, including pre-existing `trace-summary` mode.
All acceptance criteria for this iteration were met with minimal, isolated diffs.
No unrelated refactors were introduced.
Next iteration should add malformed container-shape guards for `chapters/history/latest-entry` fixtures.
