# Task

## Selected task title
Refactor duplicated shutdown-mode smoke test setup into a shared helper.

## Why this task now
`iter_034/06-next-iteration.md` identified repeated setup/teardown across shutdown-focused modes, which increases maintenance overhead for deterministic reliability coverage.

## Acceptance criteria for this iteration
- Add a shared helper to initialize/teardown shutdown-mode test clients.
- Reuse it in `shutdown-failure`, `stop-unavailable`, `destroy-failure`, and `force-stop-unavailable`.
- Preserve current mode pass behavior and outputs.
