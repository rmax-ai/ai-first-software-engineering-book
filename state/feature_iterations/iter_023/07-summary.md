# Summary

Iteration 023 implemented the ordering guard requested by iteration 022.  
`state/copilot_sdk_smoke_test.py` now includes `usage-examples-order-guard`.  
The new mode asserts generated non-`stub` usage lines preserve `_all_mode_specs()` registration order.  
Mode registration remains centralized in metadata, so parser/help/doc generation and dispatch wiring are unchanged.  
Targeted smoke validation was executed for `stub` and the new ordering guard mode, and both passed.  
The next iteration should add an explicit set/count coverage guard for generated non-`stub` usage modes.
