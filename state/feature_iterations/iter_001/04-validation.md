# Validation

## Verification commands run
- `python - <<'PY'\nfrom pathlib import Path\nbase = Path('state/feature_iterations/iter_001')\nrequired = [f'{i:02d}-{name}.md' for i, name in [(1,'task'),(2,'plan'),(3,'execution'),(4,'validation'),(5,'risks-and-decisions'),(6,'next-iteration'),(7,'summary')]]\nmissing = [p for p in required if not (base / p).exists()]\nprint('PASS' if not missing else f'FAIL missing: {missing}')\nPY`
- `rg -n "state/kernel.py|state/role_io_templates.py|state/copilot_sdk_uv_smoke.py|evals/" state/feature_iterations/iter_001/*.md`

## Observed results
- PASS: all seven required iteration artifacts are present in `state/feature_iterations/iter_001/`.
- PASS: plan artifacts explicitly reference required harness and eval file paths.

## Acceptance criteria status
1. Plan includes features/tests/evals coverage: **PASS**
2. Future file-touch scope is concrete and path-specific: **PASS**
3. Next iteration task is singular with measurable criteria: **PASS**
