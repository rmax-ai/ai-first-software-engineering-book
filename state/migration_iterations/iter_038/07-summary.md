# Summary

This iteration completed one migration hardening task from the previous handoff.
It added a deterministic `stop-close-idempotency` mode to `state/copilot_sdk_smoke_test.py`.
The new mode forces `stop()` to be unavailable, asserts first-close shutdown error detail, and validates second-close idempotency.
CLI mode usage text, mode choices, and dispatch were updated so the scenario is executable.
All deterministic non-live smoke modes were run and passed before and after the change.
Existing `stop-unavailable` mode assertions and PASS output remained unchanged.
No public kernel or client interfaces changed.
The next recommended task is idempotency coverage for the `force_stop() unavailable` shutdown branch.
