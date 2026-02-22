# Risks and Decisions

## Risks discovered
- CLI mode help text is long and easy to desynchronize from dispatch choices.

## Decisions made
- Followed existing pattern by wiring the new mode across docstring usage, mode list, help text, and dispatcher.
- Validated neighboring guard modes to reduce risk of behavior drift.

## Deferred
- No refactors to shorten argparse help text were made to keep this iteration minimal.
