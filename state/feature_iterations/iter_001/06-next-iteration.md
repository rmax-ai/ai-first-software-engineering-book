# Next iteration recommendation

## Task
Implement deterministic trace-summary logging scaffolding in `state/kernel.py` with initial smoke coverage hooks.

## Why next
The plan depends on trustworthy and structured observability first; downstream role I/O and eval updates should build on stable trace-summary outputs.

## Acceptance criteria
- Add a minimal, deterministic trace-summary emitter path in `state/kernel.py` without breaking current interfaces.
- Add or update targeted smoke coverage in `state/copilot_sdk_uv_smoke.py` to validate trace-summary presence/shape.
- Document expected metric signal impact in `state/metrics.json` (or related writer path) for regression visibility.

## Expected files to touch
- `state/kernel.py`
- `state/copilot_sdk_uv_smoke.py`
- `state/metrics.json`
