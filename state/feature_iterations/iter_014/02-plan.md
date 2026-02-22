# Plan
1. Add a `TRACE_SUMMARY_MODE_SPECS` table in `state/copilot_sdk_smoke_test.py` containing mode names, handlers, and help descriptions.
2. Reuse this table for argparse `--mode` choices and trace-summary dispatch.
3. Build trace-summary help text from the same table to remove duplicated strings.
4. Run targeted smoke validations and syntax check for the touched file.
