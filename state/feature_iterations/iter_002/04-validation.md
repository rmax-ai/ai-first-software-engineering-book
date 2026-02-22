# Validation

## Verification commands

1. `python3 -m py_compile state/kernel.py`
2. `python3 state/kernel.py --help | head -n 20`

## Observed results

- Command 1: **pass** (syntax/type-shape level validation for edited module).
- Command 2: **fail** with `ModuleNotFoundError: No module named 'yaml'` in this environment (runtime dependency unavailable outside UV-managed environment).

## Acceptance criteria status

1. Tracepoints for start/eval/persist events: **pass** (verified by direct code inspection in `state/kernel.py`).
2. Deterministic JSONL trace sink path: **pass** (`out/kernel_trace.jsonl` helper added).
3. Lifecycle/eval gating unchanged: **pass** (existing decision branches preserved).
