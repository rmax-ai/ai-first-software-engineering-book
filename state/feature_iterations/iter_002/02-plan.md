# Plan

1. Add a small helper in `state/kernel.py` to append JSONL trace entries to each iteration directory.
2. Emit trace events at three points in `run_kernel`: loop start, post-eval decision, and post-ledger persistence.
3. Run targeted verification (`python3 -m py_compile state/kernel.py`) and record runtime caveats.

## Files expected to change

- `state/kernel.py`
- `state/feature_iterations/iter_002/*.md`
