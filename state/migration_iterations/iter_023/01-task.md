# Task

## Selected task title
Add deterministic regression coverage for HTTP fallback connection-failure mapping.

## Why this task now
`iter_022/06-next-iteration.md` marked connection-failure mapping as the next uncovered fallback failure mode.

## Acceptance criteria for this iteration
- A new smoke mode forces fallback transport failure without external dependencies.
- The failure message includes `HTTP fallback connection failed`.
- The mode exits non-zero if the mapping regresses.
