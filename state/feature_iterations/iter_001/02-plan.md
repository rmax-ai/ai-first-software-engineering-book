# Plan

1. Audit harness seams referenced by `DEVELOPMENT.md` and define the smallest backlog item that improves determinism and observability first.
2. Specify `state/kernel.py` changes:
   - Introduce a normalized phase-trace summary helper with strict shape validation.
   - Emit clearer failure metadata for budget/validator failures without changing public CLI flags.
3. Specify `state/role_io_templates.py` changes:
   - Add explicit template contract notes for role input/output placeholders.
   - Add one deterministic guard for missing required sections.
4. Specify `state/copilot_sdk_uv_smoke.py` changes:
   - Add one table-driven smoke mode validating the new trace summary behavior.
   - Keep smoke matrix deterministic and aligned with existing naming conventions.
5. Specify eval updates (`evals/*.yaml`):
   - Add/adjust one focused check that verifies expected trace signal fields.
   - Ensure no overlap with existing style/drift guards.
6. Define verification sequence for execution iteration:
   - `uv run python state/copilot_sdk_uv_smoke.py --mode <new-mode>`
   - targeted kernel invocation against a small chapter fixture
   - existing eval gate command(s) used by repository workflow.

## Expected files to change in future execution iteration
- `state/kernel.py`
- `state/role_io_templates.py`
- `state/copilot_sdk_uv_smoke.py`
- `evals/*.yaml` (one targeted file expected)
- `state/feature_iterations/iter_002/*.md`
