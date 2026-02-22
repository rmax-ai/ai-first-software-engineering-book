# Risks and decisions

## Risks discovered
- The new guard enforces containment only (`mode_name in pass_message`), so wrappers could still drift on surrounding PASS message phrasing while preserving mode-name inclusion.

## Decisions made and trade-offs
- Kept this iteration narrowly scoped to the task from `iter_096` guidance and avoided stricter formatting assertions to preserve minimal-diff delivery.
- Ran targeted duplicate-count smoke validations to verify the changed guard path and baseline wrapper coverage mode.

## Deferred items
- Exact PASS message formatting/prefix canonicalization remains deferred to a follow-up guard.
