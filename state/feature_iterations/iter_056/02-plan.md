# Plan

1. Add a small deterministic fixture builder in `state/copilot_sdk_uv_smoke.py` that writes synthetic metrics and kernel trace data under a controlled fixture root.
2. Route `--mode trace-summary` to that fixture by default when `--run-kernel-for-trace-summary` is not set.
3. Keep existing kernel-backed trace-summary behavior intact when the kernel flag is enabled.
4. Run a targeted smoke command and record concrete output in iteration artifacts.

## Files expected to change
- `state/copilot_sdk_uv_smoke.py`
- `state/feature_iterations/iter_056/*.md`
