# Summary

Completed one focused backlog task from `iter_004`: deterministic trace-summary regression coverage in the main smoke matrix.
Added shared helpers to read latest trace-summary fixture data and check required keys.
Introduced `trace-summary` mode to assert required keys are present.
Introduced `trace-summary-missing-key` mode to assert required-key omissions are detected.
Updated CLI mode choices/help text and dispatch for both new modes.
Ran targeted validation (`py_compile` + both smoke modes) and all checks passed.
No unrelated refactors were introduced.
Next iteration should add malformed trace-summary type-shape coverage.
