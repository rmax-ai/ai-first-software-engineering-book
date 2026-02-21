# Validation

## Verification commands run
1. `python - <<'PY' ...` status check on `state/ledger.json`
2. `python state/kernel.py --chapter-id 01-paradigm-shift`
3. `python state/kernel.py --chapter-id 01-paradigm-shift --llm --llm-provider mock`

## Observed outputs/results
- Eligibility check: `status_counts {'locked': 8, 'active_refinement': 1}` and eligible chapter `('01-paradigm-shift', 'active_refinement')`.
- File-driven run failed with missing role outputs for `state/role_io/01-paradigm-shift/iter_03/out/{planner.json,writer.md,critic.json}`.
- Mock LLM run failed deterministic gate with `KernelError: Writer changed headings; this is forbidden.`

## Pass/fail against acceptance criteria
- Execute kernel regression on eligible chapter: **PASS**
- Verify planner/writer/critic path can run: **FAIL (blocked by deterministic heading gate in mock LLM path; file-driven path missing outputs)**
- Capture exact failure and bounded unblock step: **PASS**
