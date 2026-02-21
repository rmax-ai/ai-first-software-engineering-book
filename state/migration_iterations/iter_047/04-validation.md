# Validation

## Verification commands run
- `uv sync --quiet && python -c "import copilot; print('copilot import ok')"`
- `uv run python -c "import copilot; print('copilot import ok under uv run')"`
- `uv run python state/copilot_sdk_smoke_test.py --mode live`

## Observed outputs/results
- `python -c "import copilot"` failed with `ModuleNotFoundError: No module named 'copilot'`.
- `uv run python -c "import copilot"` printed `copilot import ok under uv run`.
- Live smoke output:
  - `PASS: live Copilot SDK chat works`
  - `provider=copilot model=gpt-4.1-mini`
  - `content='ok'`
  - `usage=prompt_tokens=16608, completion_tokens=29`

## Pass/fail against acceptance criteria
- PASS: Repo-managed environment can import `copilot` via `uv run`.
- PASS: Live smoke mode executed successfully and produced response + usage evidence.
- PASS: Iteration artifacts updated with explicit validation evidence.
