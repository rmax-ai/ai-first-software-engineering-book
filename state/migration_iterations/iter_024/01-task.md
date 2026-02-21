# Task

## Selected task title
Add deterministic regression coverage for HTTP fallback timeout mapping.

## Why this task now
`iter_023/06-next-iteration.md` identified timeout mapping as the next uncovered fallback failure mode.

## Acceptance criteria for this iteration
- A new smoke mode deterministically forces fallback timeout behavior.
- The error message includes `HTTP fallback timed out`.
- The mode exits non-zero if timeout mapping regresses.
