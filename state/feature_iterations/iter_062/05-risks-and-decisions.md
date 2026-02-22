# Risks and decisions

## Risks discovered
- Fixture setup now depends on a curated copy set (kernel dependencies, prompts, evals, governance, roadmap, and chapter source); future kernel dependencies may require fixture updates.
- Accepting kernel return code `1` in smoke mode could mask non-eligibility runtime failures if artifact checks are weakened.

## Decisions and trade-offs
- Chose an isolated git fixture repository instead of temporary in-place ledger edits to keep repository state immutable during smoke runs.
- Kept strict post-run artifact checks (trace summary keys and phase-trace schema validation) so relaxed kernel exit handling does not reduce validation rigor.

## Deferred
- No expansion to deterministic `state/copilot_sdk_smoke_test.py` coverage in this iteration; deferred as the next focused task.
