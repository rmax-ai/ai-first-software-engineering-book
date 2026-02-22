# Risks and decisions

## Risks discovered
- Planning quality depends on future implementation discipline; broad edits could weaken deterministic harness behavior.
- Eval coupling risk: adding checks in smoke mode without aligning `evals/*.yaml` may cause false confidence.

## Decisions made
- Kept this iteration strictly planning-only to satisfy the seed prompt and reduce churn.
- Chose a single, smallest follow-up implementation task focused on trace-summary guard wiring for fast feedback.

## Deferred intentionally
- No code changes to `state/kernel.py`, `state/role_io_templates.py`, or eval YAML files in this iteration.
- No runtime harness execution beyond artifact validation, because this iteration's deliverable is the plan itself.
