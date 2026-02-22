# Recommended next iteration

## Next task
Implement deterministic trace-summary instrumentation in `state/kernel.py` and align role IO scaffolding in `state/role_io_templates.py` to expose the new trace fields.

## Why this is next
It converts the highest-priority planning item into measurable behavior and establishes the observability baseline needed before expanding smoke and eval coverage.

## Acceptance criteria
- `state/kernel.py` emits deterministic trace-summary fields for each harness run without changing existing public CLI behavior.
- `state/role_io_templates.py` includes matching schema/template updates required by the new trace-summary output.
- Targeted verification confirms stable output shape across at least one deterministic harness run command.

## Expected files to touch
- `state/kernel.py`
- `state/role_io_templates.py`
- `state/copilot_sdk_uv_smoke.py` (if smoke assertions require updates)
