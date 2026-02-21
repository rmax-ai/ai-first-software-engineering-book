# State Runner Migration Plan: Copilot Python SDK

## Goal

Use the Copilot Python SDK as the primary LLM integration in `state/llm_client.py`, replacing the custom HTTP path for network providers while preserving existing kernel behavior, governance constraints, and ledger/resource accounting.

## Current Baseline

- `state/kernel.py` is synchronous and expects `LLMClient.chat(...) -> LLMResponse`.
- `state/llm_client.py` supports providers: `copilot`, `mock`.
- Kernel records usage via `LLMUsage(prompt_tokens, completion_tokens)` and writes to `state/ledger.json` / `state/metrics.json`.
- Deterministic local mode relies on `mock` behavior.

## Verified SDK Capabilities (local source: `/Users/rmax/Workspace/rmax-ai/copilot-sdk/python`)

- Async client lifecycle: `CopilotClient.start()/stop()/force_stop()`.
- Session lifecycle: `create_session()/resume_session()/session.destroy()`.
- Prompt execution: `session.send(...)` and event-driven completion (`session.idle`).
- Event stream includes `assistant.message`, `assistant.message_delta`, `assistant.usage`, `session.error`, and lifecycle events.
- Tools, hooks, providers, and auth are configurable in `SessionConfig` / `CopilotClientOptions`.
- SDK is async-first and does not provide built-in transport retries/backoff guarantees.

## Target Architecture

### 1) Compatibility Adapter in `state/llm_client.py`

Keep the public interface unchanged:

- `LLMClient(provider, model, base_url, api_key_env, timeout_s)`
- `chat(messages, temperature=0.0, max_tokens=None) -> LLMResponse`

Implement an internal adapter that:

- Uses Copilot SDK for the `copilot` provider.
- Maintains a single client + session per kernel run (lazy-initialized).
- Converts sync `chat(...)` calls into async SDK calls via an internal event loop bridge.
- Aggregates token usage from `assistant.usage` events into existing `LLMUsage` shape.
- Preserves `mock` provider exactly for deterministic runs.

### 2) Minimal Kernel Touch in `state/kernel.py`

- Keep planner/writer/critic call flow unchanged.
- Add bounded cleanup in the kernel run path (`client.stop()` or adapter `close()` in `finally`).
- Preserve trace writing and usage accumulation semantics.

## Phased Rollout

## M0 — Introduce Adapter (No Behavioral Change)

Scope:

- Add SDK-backed code path behind provider selection.
- Keep existing HTTP implementation as fallback path.
- Keep `mock` provider unchanged.

Acceptance criteria:

- Existing mock-based kernel runs produce identical structural outcomes.
- No CLI contract changes for `state/kernel.py`.
- `LLMUsage` schema remains unchanged in ledger outputs.

Rollback:

- Switch provider mapping back to legacy HTTP path only.

## M1 — Make SDK Primary for Network Providers

Scope:

- Route `copilot` requests through SDK session config.
- Keep sync adapter surface for kernel compatibility.

Acceptance criteria:

- One full chapter iteration in LLM mode completes (planner -> writer -> critic).
- `_llm_trace` artifacts are still produced.
- Resource usage remains valid integers and non-negative.
- Session/client shutdown is clean after run.

Rollback:

- Feature flag or provider switch to force legacy transport.

## M2 — Hardening and Reliability

Scope:

- Add robust shutdown path (`stop()` with `force_stop()` fallback).
- Add focused failure mapping to `LLMClientError` for deterministic kernel handling.
- Stabilize usage extraction fallback when usage events are absent.

Acceptance criteria:

- Interrupted/failed runs do not leak sessions/processes.
- Error messages remain actionable and mapped to `KernelError` paths.
- Repeated runs do not accumulate orphaned runtime state.

Rollback:

- Disable persistent session; recreate session per request as conservative fallback.

## Test Plan

1. **Deterministic regression**: run kernel with mock provider and verify no workflow regressions.
2. **Live provider smoke test**: run `uv run python state/copilot_sdk_smoke_test.py --mode live` with SDK-backed provider.
3. **Failure path test**: induce auth/transport failure and verify clean stop + clear error propagation.
4. **Resource accounting test**: verify prompt/completion token fields persist and stay numeric.

## Risks and Mitigations

- **Async/Sync mismatch**: isolate async complexity in adapter; keep kernel sync.
- **Usage field drift across providers**: normalize with best-effort extraction + zero fallback.
- **SDK process lifecycle edge cases**: enforce explicit teardown in `finally`.
- **Behavior drift from old HTTP client**: retain fallback path until M2 is stable.

## Open Decisions

- Keep legacy HTTP path indefinitely as fallback, or remove after M2?
    - Remove legacy HTTP path after M2, as it will no longer be needed once the SDK is fully stable and the migration is complete.
- Preferred provider mapping policy for `copilot` through SDK config.
    - Use defaults.
- Whether to expose an explicit kernel flag for SDK vs legacy transport selection.
    - No legacy transport selection.
