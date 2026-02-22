# Risks and decisions

## Risks discovered
- `state/copilot_sdk_smoke_test.py` contains many similarly named wrappers; broad replacements risk touching unintended functions.

## Decisions made and trade-offs
- Limited helper adoption to the two wrappers required by acceptance criteria to keep this iteration minimal.
- Kept all PASS strings unchanged to avoid breaking deterministic smoke expectations.

## Deferred
- Migrating the remaining `run_usage_examples_duplicate_count_mode_coverage_guard*` wrappers to the new helper was deferred to the next iteration.
