# Next iteration recommendation

## Task
Add deterministic loop self-evaluation logging to `state/kernel.py` and validate it in smoke output.

## Why this is next
`execute.md` and `AGENTS.md` require loop-level goal/evidence/risk/next-step evaluation; kernel-level logging is the smallest high-value harness feature that unlocks measurable observability.

## Acceptance criteria
- `state/kernel.py` emits one structured self-evaluation block per loop containing: goal check, evidence check, risk check, next-step decision.
- `state/copilot_sdk_uv_smoke.py` includes an assertion that self-evaluation blocks appear in expected loop outputs.
- `04-validation.md` in the new iteration records execution of `uv run python state/copilot_sdk_uv_smoke.py` with passing evidence.

## Expected files to touch
- `state/kernel.py`
- `state/copilot_sdk_uv_smoke.py`
- `state/feature_iterations/iter_002/04-validation.md`
