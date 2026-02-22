# Risks and decisions

## Risks discovered
- The parity cleanup guard family now has overlapping checks, so future edits must keep mode names and assertions synchronized.

## Decisions made and trade-offs
- Reused existing parser and usage extraction helpers to keep behavior deterministic and avoid introducing new helper abstractions in this narrow iteration.
- Added a dedicated composite mode instead of modifying existing guard modes to preserve prior validation surfaces and minimize risk.

## Intentionally deferred
- Consolidating repeated parity target-mode tuple definitions across guard functions was deferred to keep this iteration scoped to one unfinished task.
