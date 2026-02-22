# Next iteration recommendation

## Recommended next task
Implement deterministic loop self-evaluation logging in `state/kernel.py` and wire it into iteration artifacts produced by the harness.

## Why this is next
It is the smallest high-impact implementation slice from this plan and directly supports auditability requirements already defined in `AGENTS.md` and the harness execution rules.

## Acceptance criteria
- Add structured self-evaluation fields (goal/evidence/risk/decision) captured per loop.
- Ensure exhausted-loop stop paths emit a clear, bounded next action.
- Add/extend targeted checks (smoke/unit) to verify the new structured output shape.
- Document the executed verification command(s) and observed output in the new iteration's `04-validation.md`.

## Expected files to touch
- `state/kernel.py`
- `state/copilot_sdk_uv_smoke.py`
- Optional focused test helpers under `state/`
