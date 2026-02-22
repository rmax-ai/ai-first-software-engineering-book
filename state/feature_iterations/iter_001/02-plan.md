# Plan

1. Baseline current harness structure by reviewing:
   - `state/kernel.py`
   - `state/role_io_templates.py`
   - `state/copilot_sdk_uv_smoke.py`
   - `evals/chapter-quality.yaml`, `evals/style-guard.yaml`, `evals/drift-detection.yaml`
2. Define feature changes for `state/kernel.py`:
   - Add richer per-step trace fields for deterministic debugging.
   - Add explicit guardrail outcome tagging (pass/fail/blocked) for each loop stage.
3. Define role I/O scaffold improvements in `state/role_io_templates.py`:
   - Tighten template structure for role prompts and expected outputs.
   - Add stable placeholders that support deterministic replay.
4. Define smoke-test coverage in `state/copilot_sdk_uv_smoke.py`:
   - Add targeted scenarios validating new trace fields and guardrail tags.
   - Keep scenarios deterministic and runnable via `uv run`.
5. Define eval wiring updates in `evals/*.yaml`:
   - Add checks that assert trace signal presence and formatting.
   - Add regression checks tied to expected metric/ledger outputs.
6. Sequence future iterations:
   - Iteration A: kernel trace + tests
   - Iteration B: role templates + tests
   - Iteration C: smoke/eval integration and regression validation
