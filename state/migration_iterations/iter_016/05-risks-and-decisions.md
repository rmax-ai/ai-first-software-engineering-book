# Risks and Decisions

## Risks discovered
- If `session.get_messages()` omits events for the current message ID, usage can still fall back to zero.
- Event schema drift across SDK versions may still affect message/usage correlation.

## Decisions and trade-offs
- Reused existing `_response_from_sdk_events(...)` instead of adding new parsing logic to keep diff minimal.
- Kept fallback strictly conditional on missing message usage to avoid extra event fetches on normal paths.

## Deferred
- Adding a dedicated regression test that simulates `send_and_wait` returning message-only events without usage.
