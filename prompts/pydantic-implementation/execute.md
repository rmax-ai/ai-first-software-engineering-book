# Pydantic Implementation Runner Prompt

You are an autonomous engineering agent operating inside the repository.

## Primary Objective

Implement a Pydantic-powered ingestion and transit layer in the custom harness under `state/`. When external data is loaded (fixtures, kernel traces, or evaluation inputs) it must be parsed through typed Pydantic models. When that data is passed between harness components, it should move through explicit data classes (e.g., `@dataclass`) so that state transitions remain visible, type-checked, and serializable.

## Pre-flight Requirements

1. Inspect `state/` to understand how data currently enters and flows through the harness (look at `state/kernel.py`, `state/role_io_templates.py`, and any helper modules such as `state/copilot_sdk_smoke_test.py`).
2. Identify the files or canonical data blobs that are considered "external" (file-based JSON/YAML/CSV, API responses, etc.).
3. Confirm there is a consistent way to move data between harness layers and where additional structure would clarify intent.

## Execution Rules

- Pick the smallest change that touches the ingestion path and transit path simultaneously (e.g., add a Pydantic model where data is read and an annotated data class where it is forwarded).
- Preserve existing public interfaces; add wrappers/adapters if stricter typing is required.
- Keep diffs minimal: change only the files necessary to make the new structure work.
- Validate the change by running a targeted harness exercise (e.g., `python state/copilot_sdk_smoke_test.py` if it exercises the path, or another dedicated script that covers the modified surfaces).
- Document the new structure in any relevant markdown file inside `prompts/pydantic-implementation/` if needed for future iterations (e.g., how data flows should be typed and what models exist).

## Implementation Guidance

1. **External Data Parsing**: Introduce Pydantic `BaseModel` subclasses for every external payload you control (inputs, environment, evaluation results). Use `.parse_obj()` or `.model_validate()` to enforce schemas as soon as the data enters the harness. Handle validation errors explicitly and translate them into the harness logging or exception strategy.
2. **Internal Data Movement**: Create lightweight `@dataclass` objects (or frozen dataclasses when immutability helps) to represent state transfers between kernel components. Each dataclass should reference the relevant Pydantic model where appropriate to signal the relationship between external and internal representations.
3. **State Module Updates**: Update `state/kernel.py`, `state/role_io_templates.py`, or other touched modules to consume the new typed structures. Wherever you previously passed raw dictionaries or loosely typed tuples, replace them with the defined dataclasses.
4. **Serialization / Round-trip**: Ensure that converting back to raw dicts for logging, persistence, or evaluation output continues to work (use `.model_dump()` and `asdict()` as needed).

## Validation

- Run the harness-focused smoke test(s) that exercise the ingestion path. Prefer the documented script in `state/` (e.g., `python state/copilot_sdk_smoke_test.py`).
- Include the exact command(s) executed and the results (pass/fail) in the final summary so future iterations can verify reproducibility.

## Output Requirements

- Provide a concise description of what models/dataclasses were introduced and where they are used.
- List the validation commands executed and their outcomes.
- If the change requires follow-up work (additional models, additional flows), include a single next-step recommendation under a short heading (e.g., "Next Step").

## Stop Condition

Stop after you have implemented the typed ingestion/transit layer, documented the new structure, and recorded verification evidence for the validation commands. If blocked, describe the blocker, the last successful observation, and the smallest actionable unblock step.

## Typed Flow Notes

- `state/kernel.py` validates `in/planner_input.json`, `out/planner.json`, and `out/critic.json` with Pydantic payload models before use.
- `state/kernel.py` also validates `state/ledger.json` through `LedgerPayload` and materializes each iteration's planner input via `PlannerInputTransit` before writing `in/planner_input.json`.
- `state/kernel.py` now forwards validated ledger payloads between kernel setup stages through `LedgerTransit` instead of raw tuple unpacking.
- `state/kernel.py` now carries the `JSONMappingTransit` used for ledger ingestion inside `LedgerTransit`, preserving source-path and raw-JSON provenance after `LedgerPayload` parsing.
- `state/kernel.py` validates deterministic eval YAML payloads through `DeterministicEvalConfigPayload` and forwards them between evaluators via `DeterministicEvalTransit`.
- `state/kernel.py` validates `state/metrics.json` and `state/version_map.json` through `MetricsPayload` and `VersionMapPayload` before updating runtime artifacts.
- `state/kernel.py` now forwards validated metrics payloads through `MetricsTransit` before updating chapter metrics history.
- `state/kernel.py` now forwards validated version map payloads through `VersionMapTransit` before updating chapter commit pointers.
- `state/kernel.py` now carries `JSONMappingTransit` inside `MetricsTransit` and `VersionMapTransit` so source-path and raw JSON provenance remain explicit after payload parsing.
- `state/kernel.py` now validates `ROADMAP.md` ingestion through `RoadmapTextPayload` and forwards roadmap content via `RoadmapTextTransit` before hypothesis extraction.
- `state/kernel.py` now carries `ROADMAP.md` source-path and raw markdown text through `RoadmapTextTransit` so roadmap-ingestion provenance remains explicit before hypothesis extraction.
- The planner input payload is converted into a `PlannerInputTransit` dataclass before being forwarded to the planner LLM prompt.
- Metrics history entries are now forwarded through `MetricsHistoryTransit` before append/write operations.
- Planner and critic role output ingestion now forwards validated payloads through `PlannerPlanTransit` and `CriticReportTransit` before runtime evaluation checks.
- Kernel runtime logic continues consuming internal dataclasses (`PlannerPlan`, `CriticReport`) after validation.
- `state/role_io_templates.py` now validates `state/ledger.json` through `LedgerPayload` and forwards chapter data via the `TemplateContext` dataclass before template writes.
- `state/role_io_templates.py` now also forwards validated ledger payloads between template preparation steps via `LedgerTransit`.
- `state/role_io_templates.py` now validates chapter markdown file ingestion via `ChapterTextPayload` and forwards validated chapter text via `ChapterTextTransit` before template context assembly.
- `state/role_io_templates.py` now carries chapter markdown source-path and raw text through `ChapterTextTransit` so template assembly keeps chapter-text ingestion provenance explicit.
- `state/role_io_templates.py` now stores `ChapterTextTransit` directly inside `TemplateContext`, preserving chapter-text provenance through context handoff before writer template output.
- `state/governance_engine.py` now validates `state/ledger.json` through `LedgerPayload` and passes parsed ledger data between CLI handlers via `LedgerTransit`.
- `state/governance_engine.py` now validates raw `state/ledger.json` root mappings via `LedgerJSONPayload` and forwards parsed mappings through `LedgerJSONTransit` before `LedgerPayload` parsing and `LedgerTransit` forwarding.
- `state/governance_engine.py` now validates raw `state/ledger.json` text via `JSONTextPayload` and forwards source-path text through `JSONTextTransit` before JSON mapping parsing.
- `state/governance_engine.py` now forwards ledger source-path and raw JSON text through `LedgerJSONTransit` so ingestion provenance stays explicit before `LedgerPayload` parsing.
- `state/governance_engine.py` now carries `LedgerJSONTransit` inside `LedgerTransit` so source-path and raw-ledger provenance remain available after ledger payload parsing.
- `state/governance_engine.py` now parses lifecycle transition thresholds via `ChapterLifecycleRulesPayload` and forwards promotion thresholds via `PromotionRulesTransit` before lifecycle promotion computation.
- `state/governance_engine.py` now parses chapter selection strategy ordering via `ChapterSelectionStrategyPayload` and forwards lifecycle selection order via `SelectionStrategyTransit` before deterministic chapter selection.
- `state/governance_engine.py` now validates CLI argument ingestion through `GovernanceCLIArgsPayload` and forwards parsed command arguments via `GovernanceCLIArgsTransit` before command handler dispatch.
- `state/governance_engine.py` now constrains CLI command ingestion through `GovernanceCLIArgsPayload` literal command values and dispatches handlers via `GovernanceCLIArgsTransit` payload data instead of forwarding raw callable references.
- `state/copilot_sdk_uv_smoke.py` now validates trace-summary metrics and `kernel_trace.jsonl` phase payloads with Pydantic models and forwards validated values through `MetricsHistoryTransit` and `PhaseTraceTransit`.
- `state/copilot_sdk_uv_smoke.py` now validates fixture `state/ledger.json` chapter metadata with `KernelFixtureLedgerPayload` and forwards chapter setup through `KernelFixtureChapterTransit` before kernel smoke fixture writes.
- `state/copilot_sdk_uv_smoke.py` now forwards validated fixture ledgers through `KernelFixtureLedgerTransit` before extracting chapter fixture payloads.
- `state/copilot_sdk_uv_smoke.py` now validates `phase_trace` kernel trace entries via `KernelTracePhaseEntryPayload` and forwards payload objects through `KernelTracePhaseTransit` before `PhaseTraceTransit` conversion.
- `state/copilot_sdk_uv_smoke.py` now validates `kernel_trace.jsonl` ingestion via `KernelTracePayload` and forwards trace entries through `KernelTraceTransit` before phase extraction.
- `state/copilot_sdk_uv_smoke.py` now validates raw `kernel_trace.jsonl` file text via `KernelTraceTextPayload` and forwards source-path text through `KernelTraceTextTransit` before per-line JSON payload validation.
- `state/copilot_sdk_uv_smoke.py` now validates `kernel_trace.jsonl` JSON-object line mappings through `JSONLinesPayload` and forwards parsed entries via `JSONLinesTransit` before `KernelTracePayload` parsing.
- `state/copilot_sdk_uv_smoke.py` now validates each `kernel_trace.jsonl` line through `JSONLinePayload` (including source line numbers) before forwarding line mappings through `JSONLinesTransit`.
- `state/copilot_sdk_uv_smoke.py` now forwards each validated `kernel_trace.jsonl` line through `JSONLineTransit` before aggregating them into `JSONLinesTransit`.
- `state/copilot_sdk_uv_smoke.py` now validates raw `kernel_trace.jsonl` line text via `JSONLineTextPayload` and forwards line text through `JSONLineTextTransit` before per-line JSON parsing/validation.
- `state/copilot_sdk_uv_smoke.py` now carries `kernel_trace.jsonl` source-path and raw text through `KernelTraceTransit`, alongside `KernelTraceTextTransit` and `JSONLinesTransit`, so trace-ingestion provenance remains explicit after `KernelTracePayload` parsing.
- `state/copilot_sdk_uv_smoke.py` now validates Copilot SDK prompt-mode session events through `SDKSessionEventPayload` and forwards normalized event data via `SDKSessionEventTransit` before assistant content/session-error checks.
- `state/copilot_sdk_uv_smoke.py` now validates raw Copilot SDK event object attribute mappings through `SDKEventObjectPayload` and forwards sanitized mappings via `SDKEventObjectTransit` before `SDKSessionEventPayload` parsing.
- `state/copilot_sdk_uv_smoke.py` now validates `metrics.json` ingestion via `MetricsPayload` and forwards validated payloads through `MetricsTransit` before chapter history checks.
- `state/copilot_sdk_uv_smoke.py` now validates raw JSON text via `JSONTextPayload` and forwards source-path text through `JSONTextTransit` before JSON mapping parsing.
- `state/copilot_sdk_uv_smoke.py` now validates raw JSON mapping roots via `JSONMappingPayload` and forwards parsed mappings via `JSONMappingTransit` before `MetricsPayload` parsing.
- `state/copilot_sdk_uv_smoke.py` now validates fixture ledger JSON roots via `JSONMappingPayload` and forwards parsed mappings through `JSONMappingTransit` before `KernelFixtureLedgerPayload` parsing.
- `state/copilot_sdk_uv_smoke.py` now forwards JSON mapping source-path and raw JSON text through `JSONMappingTransit` so fixture and metrics ingestion provenance remains explicit.
- `state/copilot_sdk_smoke_test.py` now validates latest `trace_summary` fixture payloads through `TraceSummaryPayload` and forwards them via `TraceSummaryTransit` before key-presence checks.
- `state/copilot_sdk_smoke_test.py` now validates trace-summary metrics fixture roots through `TraceSummaryMetricsPayload` and forwards them via `TraceSummaryMetricsTransit` before chapter/history extraction.
- `state/copilot_sdk_smoke_test.py` now validates latest metrics-history entries through `TraceSummaryHistoryEntryPayload` and forwards them via `TraceSummaryHistoryEntryTransit` before trace-summary extraction.
- `state/copilot_sdk_smoke_test.py` now validates `state/ledger.json` kernel-mode snapshots through `LedgerSnapshotPayload` and forwards them via `LedgerSnapshotTransit` before unchanged-ledger assertions.
- `state/copilot_sdk_smoke_test.py` now validates raw `state/ledger.json` snapshot text through `JSONTextPayload` and forwards source-path text via `JSONTextTransit` before JSON mapping parsing.
- `state/copilot_sdk_smoke_test.py` now validates raw ledger snapshot JSON mapping roots through `JSONMappingPayload` and forwards parsed mappings via `JSONMappingTransit` before `LedgerSnapshotPayload` parsing.
- `state/copilot_sdk_smoke_test.py` now forwards ledger snapshot JSON source-path provenance through `JSONMappingTransit` before `LedgerSnapshotTransit` assembly.
- `state/copilot_sdk_smoke_test.py` now carries `JSONTextTransit` inside `JSONMappingTransit` so ledger snapshot raw-text provenance remains attached before `LedgerSnapshotTransit` assembly.
- `state/kernel.py` now validates cross-chapter markdown ingestion through `ChapterTextPayload` and forwards deterministic-eval chapter context via `OtherChaptersTransit`.
- `state/llm_client.py` now validates external `chat()` message payload lists through `ChatMessagesPayload` and forwards validated messages via `ChatMessagesTransit` before mock/Copilot provider handling.
- `state/llm_client.py` now validates Copilot SDK `send()` response dictionaries through `SDKChatResponsePayload` and forwards them via `SDKChatResponseTransit` before usage/content normalization.
- `state/llm_client.py` now validates Copilot SDK `events` response lists through `SDKEventsPayload` and forwards them via `SDKEventsTransit` before aggregating usage tokens.
- `state/llm_client.py` now validates raw SDK usage mappings through `SDKUsagePayload` and forwards normalized usage through `SDKUsageTransit` before token accounting.
- `state/llm_client.py` now normalizes every SDK event object/list entry through `SDKEventsTransit` before usage extraction, including non-dict event objects returned by SDK session APIs.
- `state/copilot_sdk_smoke_test.py` now translates `LedgerSnapshotPayload` validation failures into explicit assertion errors during ledger fixture ingestion while forwarding validated snapshots via `LedgerSnapshotTransit`.
- `state/role_io_templates.py` now validates raw JSON mapping roots through `JSONMappingPayload` and forwards parsed mappings via `JSONMappingTransit` before `LedgerPayload` parsing.
- `state/role_io_templates.py` now also forwards ledger source-path and raw JSON text through `JSONMappingTransit` so ingestion provenance stays explicit before `LedgerPayload` parsing.
- `state/kernel.py` now validates deterministic eval YAML mapping roots through `YAMLMappingPayload` and forwards parsed mappings via `YAMLMappingTransit` before `DeterministicEvalConfigPayload` parsing.
- `state/kernel.py` now validates raw deterministic eval YAML file text through `YAMLTextPayload` and forwards source-path text via `YAMLTextTransit` before YAML mapping parsing.
- `state/kernel.py` now forwards deterministic eval YAML source-path and raw YAML text through `YAMLMappingTransit` so ingestion provenance remains explicit before `DeterministicEvalConfigPayload` parsing.
- `state/kernel.py` now carries deterministic eval `YAMLMappingTransit` inside `DeterministicEvalConfigTransit` so evaluator-config provenance stays attached after config payload parsing.
- `state/kernel.py` now forwards each deterministic eval YAML payload through `DeterministicEvalConfigTransit` before composing `DeterministicEvalTransit` for evaluator execution.
- `state/kernel.py` now validates chapter-quality and style-guard deterministic eval rule payloads through `ChapterQualityEvalConfigPayload` and `StyleGuardEvalConfigPayload`, then forwards them through `DeterministicEvalRulesTransit` before deterministic evaluator checks.
- `state/kernel.py` now validates raw JSON mapping roots through `JSONMappingPayload` and forwards parsed mappings via `JSONMappingTransit` before planner/role output and runtime payload parsing.
- `state/kernel.py` now forwards JSON mapping source-path and raw JSON text through `JSONMappingTransit` so JSON ingestion provenance remains explicit before runtime payload parsing.
- `state/kernel.py` now validates planner/critic LLM JSON response ingestion through `JSONMappingPayload` and forwards parsed objects via `JSONMappingTransit` before role output persistence.
- `state/kernel.py` now validates iteration `out/planner.json` ingestion through `JSONMappingPayload` and forwards the parsed planner output via `JSONMappingTransit` before writer prompt assembly.
- `state/kernel.py` now validates raw JSON file text through `JSONTextPayload` and forwards source-path text via `JSONTextTransit` before JSON mapping parsing.
- `state/kernel.py` now validates raw planner/critic LLM JSON response text through `LLMJSONResponseTextPayload` and forwards it via `LLMJSONResponseTextTransit` before JSON object extraction.
- `state/kernel.py` now validates normalized planner/critic JSON response text through `LLMNormalizedJSONTextPayload` and forwards it via `LLMNormalizedJSONTextTransit` before JSON-object candidate detection.
- `state/kernel.py` now validates extracted planner/critic JSON object text via `LLMJSONObjectTextPayload` and forwards selected JSON slices through `LLMJSONObjectTextTransit` before JSON mapping parsing.
- `state/kernel.py` now validates critic eval input ingestion (`evals/chapter-quality.yaml`, `evals/style-guard.yaml`, `evals/drift-detection.yaml`) through `CriticEvalInputsPayload` and forwards values via `CriticEvalInputsTransit` before critic prompt assembly.
- `state/kernel.py` now validates planner/writer/critic prompt markdown ingestion through `PromptTextPayload` and forwards prompt text via `PromptTextTransit` before assembling LLM system messages.
- `state/kernel.py` now carries prompt source-path and raw prompt markdown through `PromptTextTransit` so prompt-ingestion provenance remains explicit after `PromptTextPayload` parsing.
- `state/kernel.py` now validates active chapter markdown ingestion through `ChapterTextPayload` and forwards validated text via `ChapterTextTransit` before planner input assembly and writer/diff evaluation checks.
- `state/kernel.py` now validates `out/writer.md` ingestion through `WriterOutputPayload` and forwards validated markdown via `WriterOutputTransit` before critic prompt assembly and runtime evaluation checks.
- `state/kernel.py` now validates writer LLM markdown responses through `WriterOutputPayload` and forwards validated content via `WriterOutputTransit` before persisting `out/writer.md`.
- `state/kernel.py` now carries writer-output source-path and raw markdown text through `WriterOutputTransit` so writer-ingestion provenance remains explicit after `WriterOutputPayload` parsing.
- `state/kernel.py` now validates critic eval YAML text ingestion through `YAMLTextPayload` and forwards each eval input via `YAMLTextTransit` inside `CriticEvalInputsTransit` before critic prompt assembly.
- `state/kernel.py` now carries critic-eval YAML source-path and raw YAML text through `YAMLTextTransit` so eval-input ingestion provenance remains explicit after `YAMLTextPayload` parsing.
- `state/kernel.py` now materializes `chapter_meta` from validated `LedgerChapterPayload` via `model_dump()` so chapter transit no longer reads `ledger_transit.raw` for runtime chapter state.
- `state/kernel.py` now routes cross-chapter markdown ingestion through `_load_chapter_text()` so `ChapterTextTransit` carries source-path/raw-text provenance before `OtherChaptersTransit` mapping conversion.
- `state/copilot_sdk_smoke_test.py` now validates ledger snapshot JSON roots through `_load_json_mapping()` and forwards raw JSON text plus parsed mappings via `JSONMappingTransit` before `LedgerSnapshotTransit` assembly.
- `state/llm_client.py` now validates Copilot SDK session event objects through `SDKSessionEventPayload` and forwards normalized event data via `SDKSessionEventTransit` before usage aggregation and assistant message extraction.
- `state/llm_client.py` now validates Copilot SDK session event lists through `SDKSessionEventsPayload` and forwards them via `SDKSessionEventsTransit` before per-event usage aggregation/message extraction.
- `state/llm_client.py` now routes non-dict Copilot SDK usage objects through `_sdk_usage_mapping()` so token attributes are validated by `SDKUsagePayload`/`SDKUsageTransit` before runtime usage accounting.
- `state/llm_client.py` now validates `send_and_wait()` session event responses through `SDKSessionEventPayload` and forwards normalized event data via `SDKSessionEventTransit` before immediate content/usage extraction.
- `state/llm_client.py` now validates Copilot SDK API key environment ingestion through `APIKeyEnvPayload` and forwards sanitized values via `APIKeyEnvTransit` before Copilot client options initialization.
- `state/llm_client.py` now validates raw Copilot SDK event object attribute mappings through `SDKEventObjectPayload` and forwards sanitized mappings via `SDKEventObjectTransit` before session/event payload parsing.
- `state/role_io_templates.py` now validates raw ledger JSON text through `JSONTextPayload` and forwards source-path text via `JSONTextTransit` before JSON mapping parsing.
- `state/copilot_sdk_uv_smoke.py` now validates fixture chapter mappings through `KernelFixtureChapterMappingPayload` and forwards chapter metadata via `KernelFixtureChapterMappingTransit` before `KernelFixtureChapterTransit` builds fixture ledger chapter state.
- `state/copilot_sdk_uv_smoke.py` now forwards latest validated trace-summary payloads through `TraceSummaryTransit` before required-key checks in trace-summary smoke mode.
- `state/copilot_sdk_smoke_test.py` now validates live-mode environment ingestion through `LiveModeEnvPayload` and forwards provider/model/base-url values via `LiveModeEnvTransit` before `LLMClient` initialization.
- `state/copilot_sdk_smoke_test.py` now validates per-chapter metrics history entries through `TraceSummaryChapterMetricsPayload` and forwards latest entries via `TraceSummaryChapterMetricsTransit` before trace-summary extraction.
- `state/copilot_sdk_smoke_test.py` now validates CLI argument ingestion through `SmokeCLIArgsPayload` and forwards parsed values via `SmokeCLIArgsTransit` before mode dispatch.
- `state/role_io_templates.py` now validates CLI argument ingestion through `TemplateCLIArgsPayload` and forwards parsed values via `TemplateCLIArgsTransit` before ledger iteration resolution and template writes.
- `state/copilot_sdk_uv_smoke.py` now validates CLI argument ingestion through `SmokeCLIArgsPayload` and forwards parsed values via `SmokeCLIArgsTransit` before mode dispatch and trace-summary runner setup.
- `state/kernel.py` now validates CLI argument ingestion through `KernelCLIArgsPayload` and forwards parsed values via `KernelCLIArgsTransit` before chapter listing, LLM config validation, and `run_kernel()` dispatch.
