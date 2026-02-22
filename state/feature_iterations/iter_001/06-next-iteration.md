# Next iteration recommendation

## Task
Implement deterministic trace-summary schema guards in `state/kernel.py` and add matching smoke coverage in `state/copilot_sdk_smoke_test.py`.

## Why this is next
Trace-summary guardrails are foundational for reliable observability and will reduce risk before broader harness control changes are introduced.

## Acceptance criteria
- Add or tighten helper validation in `state/kernel.py` that enforces trace summary container and latest-entry shape invariants.
- Extend deterministic smoke matrix in `state/copilot_sdk_smoke_test.py` with at least one focused mode exercising the new guard path.
- Run targeted verification demonstrating the new mode passes and existing deterministic smoke modes still pass.

## Expected files to touch
- `state/kernel.py`
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_002/03-execution.md`
- `state/feature_iterations/iter_002/04-validation.md`
