# Summary

Iteration 022 implemented the duplicate-line hardening requested by iteration 021.  
`state/copilot_sdk_smoke_test.py` now includes `usage-examples-duplicates-guard`.  
The guard extracts generated usage command lines and asserts uniqueness for all non-`stub` mode lines.  
Mode registration remains centralized in `TRACE_SUMMARY_MODE_SPECS`, preserving parser/help/doc generation behavior.  
Targeted smoke validations passed for `stub` and the new duplicates guard mode.  
The next iteration should add an explicit ordering guard for generated usage lines.
