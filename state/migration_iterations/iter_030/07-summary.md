# Summary

This iteration completed one migration task from the prior handoff.
A new deterministic smoke-test mode, `bootstrap-failure`, was added to `state/copilot_sdk_smoke_test.py`.
The mode forces worker-loop bootstrap failure and asserts `Copilot SDK worker-loop bootstrap` error context.
CLI docs and argparse routing were updated so the mode is discoverable and runnable.
Validation was executed for `stub`, `sdk-unavailable`, and `bootstrap-failure` in a single command chain.
All three modes passed.
The implementation stayed minimal and limited to smoke-test coverage only.
No production SDK adapter behavior or public interfaces were changed.
