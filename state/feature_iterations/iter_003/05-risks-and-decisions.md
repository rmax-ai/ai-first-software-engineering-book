# Risks and Decisions

## Risks discovered
- Metrics history growth may increase file size over long runs.
- Consumers that hard-code exact key sets may ignore new data until updated.

## Decisions and trade-offs
- Implemented additive `trace_summary` field to avoid schema breakage.
- Reused existing computed values (`pass_now`, `det_pass`, `diff_ratio`, `det.drift_score`) to keep behavior deterministic.

## Deferred intentionally
- No schema contract file update in this iteration.
- No additional smoke assertions for trace summary payload yet.
