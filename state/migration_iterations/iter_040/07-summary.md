# Summary

This iteration completed one migration hardening task from the previous handoff.
It added deterministic `destroy-unavailable` smoke coverage in `state/copilot_sdk_smoke_test.py`.
The new mode patches `session.destroy` to non-callable and verifies `close()` succeeds on that path.
CLI usage text, parser choices, help text, and dispatch were updated to expose the new mode.
All deterministic non-live smoke modes were executed and passed after the change.
Existing `destroy-failure` assertions and PASS output remained unchanged.
No public kernel or client interfaces changed.
Next iteration should add idempotency coverage for repeated close calls under the same non-callable destroy branch.
