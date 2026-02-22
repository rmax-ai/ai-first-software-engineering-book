# Risks and Decisions

## Risks discovered
- Planning-only iteration does not prove runtime behavior yet; implementation could reveal integration gaps.
- Existing smoke/eval contracts may require minor interpretation when mapping new harness telemetry.

## Decisions made
- Chose strict planning scope to satisfy the seed iteration requirement from the execution prompt.
- Focused backlog on minimal, high-leverage harness surfaces: kernel tracing, role IO contract checks, and deterministic smoke assertions.

## Deferred intentionally
- Any code changes in `state/kernel.py`, `state/role_io_templates.py`, or `state/copilot_sdk_uv_smoke.py`.
- Any updates to `evals/*.yaml` until implementation iteration establishes concrete new signals.
