# Next iteration recommendation

## Task
Implement deterministic trace outcome tagging in `state/kernel.py` with targeted tests.

## Why next
- It is the highest-leverage foundation for observability and enables later smoke/eval assertions.

## Acceptance criteria
- Add explicit per-stage outcome tags (`pass`, `fail`, `blocked`) to kernel trace records.
- Preserve current public CLI behavior and command-line interface.
- Add/adjust targeted tests or deterministic smoke checks proving tags are emitted in success and failure paths.
- Document validation commands and outputs in the next iteration artifacts.

## Expected files to touch
- `state/kernel.py`
- `state/copilot_sdk_uv_smoke.py` (or targeted state test module if present)
- `state/feature_iterations/iter_002/*.md`
