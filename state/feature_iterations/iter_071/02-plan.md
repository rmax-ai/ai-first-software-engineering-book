# Plan

1. Inspect existing parity cleanup usage-example guard logic in `state/copilot_sdk_smoke_test.py` and mirror its structure for parser-choice checks.
2. Implement one new deterministic mode function that:
   - reads argparse `--mode` choices,
   - filters both parity cleanup mode names,
   - compares their relative ordering to generated usage examples.
3. Register the new mode in `TRACE_SUMMARY_MODE_SPECS`.
4. Run targeted smoke validations for the new mode plus existing mode/doc coverage guards.
5. Document execution, validation evidence, risks, and a single next task in this iteration folder.

## Files expected to change
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_071/01-task.md`
- `state/feature_iterations/iter_071/02-plan.md`
- `state/feature_iterations/iter_071/03-execution.md`
- `state/feature_iterations/iter_071/04-validation.md`
- `state/feature_iterations/iter_071/05-risks-and-decisions.md`
- `state/feature_iterations/iter_071/06-next-iteration.md`
- `state/feature_iterations/iter_071/07-summary.md`
