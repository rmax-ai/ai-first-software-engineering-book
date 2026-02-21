# Summary

This iteration completed one migration hardening task from the previous handoff.
It added a deterministic `force-stop-close-idempotency` mode to `state/copilot_sdk_smoke_test.py`.
The new mode forces `stop()` to fail, makes `force_stop()` unavailable, asserts first-close shutdown error detail, and verifies second-close idempotency.
CLI usage text, parser choices, and dispatch were updated so the scenario is runnable.
All deterministic non-live smoke modes were run and passed before and after the change.
Existing `force-stop-unavailable` assertions and PASS output remained unchanged.
No public kernel or client interfaces changed.
The next recommended task is deterministic coverage for non-callable `session.destroy()` shutdown handling.
