# Next Iteration Recommendation

## Recommended next task
Implement deterministic kernel trace enrichment in `state/kernel.py`.

## Why this is next
- It provides the observability foundation needed before tightening smoke assertions and eval signals.
- It is a small, high-leverage slice that can be validated with targeted harness tests.

## Acceptance criteria
1. `state/kernel.py` emits structured trace records for each major loop phase and gate decision.
2. Failure traces include explicit reason codes for budget/eval/validation stops.
3. Existing kernel behavior remains intact (no public interface drift).
4. Validation includes a targeted run (for example: `uv run python state/kernel.py --chapter-id <id>`) and records observed trace evidence.

## Expected files to touch
- `state/kernel.py`
- `state/copilot_sdk_uv_smoke.py` (only if trace assertions are added immediately)
- `state/feature_iterations/iter_002/*` artifacts
