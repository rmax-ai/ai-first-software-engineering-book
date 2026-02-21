# Iteration Summary

This iteration completed one migration hardening task from the Copilot SDK plan.
A deterministic regression scenario was added in `state/copilot_sdk_smoke_test.py` for the `send_and_wait` fallback path.
The stub now returns an `assistant.message` event without usage and separate `assistant.usage` event data.
The existing smoke assertions verified that usage recovery still reports `prompt_tokens=7` and `completion_tokens=3`.
Validation passed with `uv run python state/copilot_sdk_smoke_test.py`.
No production interface changes were made.
The iteration artifacts were recorded under `state/migration_iterations/iter_017/`.
