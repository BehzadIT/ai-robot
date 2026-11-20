---
story_id: US-006
plan_version: 1
updated: "2026-11-19"
tasks:
  - id: T001
    title: Capture the migration baseline and protected invariants
    status: planned
    depends_on: []
    parallel_safe: false
    repositories: [parent, esp32]
    subsystems: [esp32-toolchain, transport-contracts, verification]
    acceptance: [AC-003, AC-006, AC-011]
    test_mode: characterization
    evidence_levels: [static, host]
    test_support: []
    baseline:
      behavior: Record the 5.5 doctor result, tracked configuration and lock identities, named sdkconfig invariants, interface files, current repository identities, and legacy installation inventory without changing them.
      command: "python3 tools/robot.py doctor --platform esp32 --json"
  - id: T002
    title: Implement exact ESP-IDF 6.1.1 discovery and reporting
    status: planned
    depends_on: [T001]
    parallel_safe: true
    repositories: [esp32]
    subsystems: [agent-adapter, eim-integration]
    acceptance: [AC-005, AC-011]
    test_mode: tdd
    evidence_levels: [host]
    test_support:
      - kind: fixture
        seam: Temporary EIM registry and fake ESP-IDF installation directories
        purpose: Exercise selected-installation parsing and IDF_PATH precedence without changing the real registry.
        limitation: A fixture cannot prove that the installed EIM activation script works.
      - kind: mock
        seam: Adapter command runner
        purpose: Return controlled idf.py version output and activation failures.
        limitation: Process mocking does not qualify the real ESP-IDF Python environment.
    red:
      test: Selection tests require IDF_PATH precedence, EIM selected-entry fallback, explicit missing or malformed registry failures, unfinished-entry rejection, and exact activated version 6.1.1.
      expected_failure: The current adapter falls back to /home/behzad/Projects/esp-idf and reports a configured 5.5 constant.
      command: "python3 -m unittest discover -s tests -p 'test_robot_adapter.py'"
    green:
      implementation: Refactor SDK discovery behind testable functions, remove the hard-coded 5.5 fallback, activate only the resolved installation, parse actual idf.py --version output, and fail closed unless it is exactly v6.1.1.
      command: "python3 -m unittest discover -s tests -p 'test_robot_adapter.py'"
    refactor_boundary: Preserve the adapter result schema, scenario identifiers, Gate 1 behavior, and ESP-IDF as the authoritative command runner.
  - id: T003
    title: Migrate ESP-IDF component declarations and generated state
    status: planned
    depends_on: [T001]
    parallel_safe: true
    repositories: [esp32]
    subsystems: [cmake-components, sdkconfig, component-manager]
    acceptance: [AC-001, AC-002, AC-003, AC-004, AC-011]
    test_mode: tdd
    evidence_levels: [static, host]
    test_support:
      - kind: fixture
        seam: Empty out-of-tree ESP-IDF build directory under parent temp/us006
        purpose: Prevent a prior 5.5 CMake cache or generated file from masking migration errors.
        limitation: Compilation does not verify device, Wi-Fi, Bluetooth, UART, or lwIP runtime behavior.
    red:
      test: Toolchain invariant tests and an ESP-IDF 6.1.1 clean configure/build reject 5.5 identities, legacy aggregate driver dependencies, obsolete project Kconfig values, and missing direct split-component dependencies.
      expected_failure: The tracked 5.5 sdkconfig and lock file fail version assertions and ESP-IDF 6.1.1 exposes migration errors before the declarations are corrected.
      command: "python3 -m unittest discover -s tests -p 'test_toolchain_migration.py'"
    green:
      implementation: Declare esp_driver_uart and every subsequently exposed ESP-IDF 6 dependency at its direct consumer, regenerate sdkconfig and dependencies.lock with 6.1.1 for classic esp32, and reconcile only obsolete Kconfig names while preserving the baseline behavior matrix.
      command: "bash -lc 'source /home/behzad/.espressif/tools/activate_idf_v6.1.1.sh >/dev/null && idf.py -B /home/behzad/Projects/ai-robot/temp/us006/build-precleanup build'"
    refactor_boundary: Do not change C runtime sources, protocol payloads, UART pins, heartbeat constants, partition intent, transport ownership, or add an ESP-IDF 5.5 compatibility branch.
  - id: T004
    title: Lock migration invariants and update toolchain documentation
    status: planned
    depends_on: [T002, T003]
    parallel_safe: false
    repositories: [parent, esp32]
    subsystems: [toolchain-documentation, migration-regression-tests]
    acceptance: [AC-003, AC-004, AC-005, AC-006]
    test_mode: tdd
    evidence_levels: [static, host]
    test_support:
      - kind: fixture
        seam: Tracked sdkconfig, dependencies.lock, CMake declarations, and documentation files
        purpose: Assert exact baseline identity and protected configuration/interface facts.
        limitation: Text assertions cannot demonstrate runtime behavior or prove every generated default is equivalent.
    red:
      test: Regression checks reject 5.5 references, wrong lock identity, missing protected configuration values, aggregate driver dependencies at affected consumers, and documentation that does not name 6.1.1 as the sole baseline.
      expected_failure: Current tracked files still identify 5.5 and the controller transport and BTstack declarations retain legacy driver dependencies.
      command: "python3 -m unittest discover -s tests -p 'test_*.py'"
    green:
      implementation: Add focused invariant checks and update ESP32-local and parent toolchain documentation, including the direct-dependency learning note, without rewriting command, telemetry, controller, wiring, or ownership contracts.
      command: "python3 -m unittest discover -s tests -p 'test_*.py'"
    refactor_boundary: Keep generated SDK state in sdkconfig and dependencies.lock; keep durable operational explanations in platform or shared docs rather than source comments.
  - id: T005
    title: Qualify the complete host migration from an empty build directory
    status: planned
    depends_on: [T004]
    parallel_safe: false
    repositories: [parent, esp32]
    subsystems: [host-verification, agent-adapter, esp-idf-build]
    acceptance: [AC-001, AC-002, AC-003, AC-004, AC-005, AC-006, AC-011]
    test_mode: characterization
    evidence_levels: [static, host, runtime]
    test_support:
      - kind: fixture
        seam: Fresh pre-cleanup build directory under temp/us006
        purpose: Demonstrate that no old build cache is required.
        limitation: Host output is not device qualification and cannot unlock cleanup by itself.
    baseline:
      behavior: The real EIM-selected installation activates as 6.1.1; adapter tests, adapter doctor, parent doctor, invariant checks, clean configuration, and compilation all pass with retained output and no project-owned dependency or obsolete-Kconfig diagnostics.
      command: "python3 -m unittest discover -s tests -p 'test_*.py' && python3 tools/robot_adapter.py doctor --json && python3 ../tools/robot.py doctor --platform esp32 --json"
  - id: T006
    title: Create and dry-review the isolated device qualification procedure
    status: planned
    depends_on: [T005]
    parallel_safe: false
    repositories: [parent, esp32]
    subsystems: [device-procedure, evidence-capture]
    acceptance: [AC-007, AC-008, AC-009, AC-010, AC-011]
    test_mode: static-only
    evidence_levels: [static]
    test_support: []
    static_check:
      method: Review a US-006 procedure containing exact-device resolution, Gate 1 approval, isolation, boot/Wi-Fi/WebSocket/UART/Bluetooth/heartbeat checks, failure classification, stop conditions, artifact names, and append-only evidence instructions.
      command: "python3 tools/docs/validate_backlog.py && python3 tools/docs/validate_us002_records.py"
  - id: T007
    title: Flash the exact ESP32 and qualify repeated boot and Wi-Fi recovery
    status: planned
    depends_on: [T006]
    parallel_safe: false
    repositories: [parent, esp32]
    subsystems: [esp32-device, wifi, serial-logging]
    acceptance: [AC-007, AC-008, AC-011]
    test_mode: physical-procedure
    evidence_levels: [device, bench]
    test_support: []
    physical:
      approval_gate: Gate 1 after passive discovery resolves exactly one owner-confirmed ESP32 serial identity; approval applies only to the named port and 6.1.1 image.
      safe_setup: ESP32 and, when needed, Pico use logic/USB power on a power-isolated bench; traction and motor-driver power are physically disconnected and the existing UART wiring is not changed.
      stop_conditions: [Serial identity changes or is ambiguous, traction or motor power is present, any unexpected motion occurs, wiring becomes hot or smells abnormal, repeated reset or brownout behavior appears, the flash or any boot/Wi-Fi check fails or is inconclusive]
      expected_result: The image flashes to the confirmed device; three USB power cycles and three software resets produce the expected serial boot sequence; three Wi-Fi loss/recovery cycles reconnect without manual firmware intervention.
      evidence_destination: A new append-only docs/verification/evidence/EV-YYYY-NNN bundle linked to US-006 and component-esp32-dev-board-01.
  - id: T008
    title: Qualify two-client WebSocket telemetry and Pico UART log forwarding
    status: planned
    depends_on: [T007]
    parallel_safe: false
    repositories: [parent, esp32, pico]
    subsystems: [websocket-telemetry, pico-log-uart, integration]
    acceptance: [AC-007, AC-009, AC-011]
    test_mode: physical-procedure
    evidence_levels: [device, bench, hil]
    test_support: []
    physical:
      approval_gate: Continue only under the still-valid Gate 1 device approval and unchanged power-isolated setup; reconnect or re-identify any device before proceeding.
      safe_setup: Keep traction and motor power disconnected; power only the named ESP32 and Pico logic; use two independent websocat clients and the existing Pico debug UART connection.
      stop_conditions: [Either device identity is ambiguous, motor power is present, UART wiring differs from the documented existing harness, either client corrupts or stalls the other, Pico log forwarding fails, any unexpected motion or unsafe electrical symptom occurs]
      expected_result: Both clients receive readiness and live frames; at least ten named Pico log lines reach both clients; disconnecting either client leaves the other receiving; no command or telemetry schema changes are observed.
      evidence_destination: The same new US-006 append-only evidence bundle, with separate raw captures for ESP32 serial and both WebSocket clients.
  - id: T009
    title: Qualify Bluetooth reconnection and repeated-state controller heartbeat transport
    status: planned
    depends_on: [T008]
    parallel_safe: false
    repositories: [parent, esp32, pico]
    subsystems: [bluepad32, controller-uart, pico-freshness]
    acceptance: [AC-007, AC-010, AC-011]
    test_mode: physical-procedure
    evidence_levels: [device, bench, hil]
    test_support: []
    physical:
      approval_gate: Continue only under the still-valid Gate 1 approval with the owner-confirmed neutral controller and unchanged isolated bench.
      safe_setup: Traction and motor power remain physically disabled; controller inputs remain neutral; existing controller UART wiring is unchanged; ESP32 and Pico diagnostics are captured concurrently.
      stop_conditions: [Controller cannot be confirmed neutral, any motion-capable power is present, pairing or any of three reconnect cycles fails, Pico reports malformed or stale transport while the controller is connected and steady, frame counters do not advance, any unexpected motion or unsafe symptom occurs]
      expected_result: Initial pairing and three disconnect/reconnect cycles succeed; controller state changes reach Pico; with controls steady for 30 seconds the Pico receiver frame count continues increasing and freshness never becomes stale; source review still shows a 100 ms heartbeat period and unchanged frame contract.
      evidence_destination: The same new US-006 append-only evidence bundle, including ESP32/Pico logs and before/after Pico receiver status snapshots.
  - id: T010
    title: Re-audit legacy material and retain the cleanup dry run
    status: planned
    depends_on: [T009]
    parallel_safe: false
    repositories: [parent, esp32]
    subsystems: [legacy-audit, cleanup-planning]
    acceptance: [AC-011, AC-012, AC-014]
    test_mode: characterization
    evidence_levels: [static, host]
    test_support: []
    baseline:
      behavior: Re-read legacy Git status; prove components/btstack is content-equivalent to the vendored project component and top-level hello_world is equivalent to the tracked upstream example; enumerate exact 5.5 registry, checkout, environment, constraints, tool, and archive targets; retain the 6.1.1 idf_tools.py uninstall --dry-run output. Any difference aborts cleanup.
      command: "git -C /home/behzad/Projects/esp-idf status --short --untracked-files=all && diff -qr /home/behzad/Projects/esp-idf/components/btstack robot-esp32-platform/components/btstack && diff -qr /home/behzad/Projects/esp-idf/hello_world /home/behzad/Projects/esp-idf/examples/get-started/hello_world"
  - id: T011
    title: Back up the registry and execute the explicitly approved cleanup
    status: planned
    depends_on: [T010]
    parallel_safe: false
    repositories: [parent]
    subsystems: [eim-registry, external-toolchain-cleanup]
    acceptance: [AC-013, AC-014]
    test_mode: characterization
    evidence_levels: [static, host]
    test_support: []
    baseline:
      behavior: Before deletion, an ignored temp/us006 backup and its hash exist, the exact absolute deletion manifest matches T010, all device checks passed, no unique material was found, the dry-run targets were reviewed, and the owner explicitly approved that manifest. Delete no target outside the manifest and stop on any mismatch.
      command: "test -f temp/us006/eim_idf.pre-cleanup.json && test -f temp/us006/cleanup-manifest.txt && test -f temp/us006/idf-tools-uninstall-dry-run.txt"
  - id: T012
    title: Prove the sole 6.1.1 state and record the integrated result
    status: planned
    depends_on: [T011]
    parallel_safe: false
    repositories: [parent, esp32]
    subsystems: [post-cleanup-verification, integrated-snapshot, evidence]
    acceptance: [AC-015]
    test_mode: characterization
    evidence_levels: [static, host, runtime]
    test_support:
      - kind: fixture
        seam: Second fresh post-cleanup build directory under temp/us006
        purpose: Prove the successful build does not depend on pre-cleanup artifacts or caches.
        limitation: The post-cleanup build complements but does not replace the retained device evidence from T007 through T009.
    baseline:
      behavior: EIM selects and activates exactly 6.1.1; scoped project and shell searches find no active 5.5 reference; adapter and parent doctor pass; all adapter/invariant tests pass; a second empty-directory build passes; the child ESP32 commit and parent pointer/docs/evidence identify the qualified combination.
      command: "python3 robot-esp32-platform/tools/robot_adapter.py doctor --json && python3 tools/robot.py doctor --platform esp32 --json && python3 tools/docs/validate_backlog.py && python3 tools/docs/validate_us002_records.py"
---
# US-006 Implementation Plan

## Architecture And Boundaries

The change belongs to the ESP32 platform because ESP-IDF, component ownership,
generated configuration, and the platform adapter are ESP32 build/runtime
concerns. The parent workspace owns the shared baseline, approval/evidence
procedure, and integrated submodule identity. Pico participates only as the
existing hardware-in-the-loop consumer of log and controller UART traffic; no
Pico or Android production behavior is changed.

The preserved architecture is:

- ESP32 owns Wi-Fi/WebSocket, Bluetooth connectivity and normalization,
  telemetry transport, controller UART transport, diagnostics, and SDK support.
- Pico owns admission, freshness, stop/recover behavior, motor output, encoders,
  timing-sensitive control, and final safety authority.
- SDK migration failures remain build or transport failures. They must not be
  handled by adding safety decisions, synthesized drive state, or compatibility
  logic to the ESP32.

The implementation uses an Adapter pattern for SDK discovery, direct dependency
declarations at component boundaries, generated configuration checked by named
behavioral invariants, and staged verification. This follows fail-closed version
selection, reproducible clean builds, and evidence-depth separation.

## Pattern Analysis

- **Reuse:** Keep the structured ESP32 adapter result schema, parent
  `tools/robot.py` discovery and approval concepts, ESP-IDF's own `idf.py` and
  `idf_tools.py`, the append-only evidence schema, existing UART/WebSocket
  contracts, and the current Bluepad32 custom platform.
- **Extend:** Add a unit-test seam around adapter discovery/version execution,
  focused tracked-file invariants, an isolated US-006 device procedure, and
  explicit ESP-IDF 6.1.1 documentation.
- **Adapt:** Translate EIM registry version 3.0's selected finished entry into
  the adapter's existing SDK-root abstraction, with `IDF_PATH` retaining
  explicit precedence. Adapt legacy aggregate `driver` dependencies to the
  ESP-IDF 6 split-component model at each direct consumer.
- **Replace:** Remove the hard-coded `/home/behzad/Projects/esp-idf` fallback,
  5.5 messages/identity, legacy affected `driver` dependencies, and generated
  5.5 configuration/lock state. Remove the actual 5.5 installation only after
  device qualification and destructive approval.
- **No precedent:** The ESP32 repository has no adapter unit-test suite and no
  single existing scenario qualifies boot, Wi-Fi recovery, two WebSocket
  clients, Pico UART, Bluetooth reconnect, and repeated-state heartbeat. Use
  standard-library `unittest` and one reusable procedure rather than introduce
  a new test framework or pretend host mocks are device evidence.

Detailed analysis and rejected alternatives are retained in
[materials/pattern-analysis.md](materials/pattern-analysis.md).

## Change Map

| Repository | Expected paths | Change purpose |
| --- | --- | --- |
| ESP32 | `components/btstack/CMakeLists.txt`, `components/controller_transport/CMakeLists.txt`, and only other consumers exposed by the v6 build | Replace aggregate/transitive reliance with direct ESP-IDF 6 split-component dependencies. |
| ESP32 | `sdkconfig`, `dependencies.lock` | Regenerate authoritative 6.1.1 state for classic `esp32` while preserving named behavior. |
| ESP32 | `tools/robot_adapter.py`, new `tests/test_robot_adapter.py`, new focused migration test | Select EIM/`IDF_PATH`, report the actual version, reject non-6.1.1, and prevent regression. |
| ESP32 | `README.md`, `docs/README.md` or the smallest appropriate platform toolchain section | Declare the sole baseline and direct-dependency rule without duplicating shared architecture. |
| Parent | `docs/reference/toolchain-requirements.yaml`, US-006 procedure/evidence/story files | Record the shared baseline, qualification contract, results, and integrated identity. |
| Parent | Submodule pointer after the ESP32 commit is qualified | Record the tested child revision; do not couple unrelated child releases. |
| Outside workspace | Exact T010 manifest only | Back up registry, then remove approved 5.5 artifacts and reviewed tools only after all gates pass. |

No Android production file, Pico production file, protocol document, wiring
document, or motor/safety behavior should change. If implementation discovers
that one must change, stop and return the story to planning.

## Diagram Index

- [Migration gates](diagrams/migration-gates.svg) shows why device success must
  precede cleanup and why every failure retains 5.5.
- [Task graph](diagrams/task-graph.svg) is the executable dependency DAG.

## Test Strategy And Doubles

TDD applies where behavior can be isolated: adapter selection/version handling
and tracked migration invariants. Tests use temporary EIM registries, fake SDK
roots, and a mocked command runner. They never modify the live EIM registry and
cannot qualify a real activation.

The ESP-IDF 6.1.1 clean build is a host/runtime integration check in a new
`temp/us006` build directory. The first build provides pre-cleanup evidence; a
different empty directory provides post-cleanup evidence. Neither is device
evidence.

The real ESP32, Pico, controller, Wi-Fi network, serial links, and two
`websocat` processes are not doubles. Device results are retained separately.
No registered logic analyzer or UART timing instrument is available, so the
heartbeat claim combines: the unchanged `100 ms` source constant and frame
contract, advancing Pico receiver frame counts during 30 seconds of steady
input, and absence of Pico stale-input transitions. This verifies the actual
repeated-state transport without claiming an instrumented per-edge jitter
measurement.

Wi-Fi credentials and other secrets must not enter logs or evidence. Evidence
promotion includes the ESP32 and Pico commit identities, actual ESP-IDF 6.1.1
identity, `US-006`, `component-esp32-dev-board-01`, and `Q-US002-004` where the
board identity observation is relevant.

## Task Graph

`T001 --> {T002, T003} --> T004 --> T005 --> T006 --> T007 --> T008 --> T009 --> T010 --> T011 --> T012`

Only T002 and T003 are parallel-safe: they touch disjoint adapter/test and
CMake/generated-state files after the immutable baseline is captured. T004
serializes integration. All device and cleanup work is deliberately serial.

## Detailed Tasks

- **T001:** Create `temp/us006/` and retain the pre-change doctor output,
  repository identities, EIM registry inventory, 5.5 installation inventory,
  relevant `sdkconfig` values, lock file, component declarations, and hashes or
  diffs of the protected protocol/transport files. This is a snapshot, not
  proof that 5.5 behavior is correct.
- **T002:** Write failing selection/version tests first. Make registry location
  and process execution injectable, distinguish missing/malformed/unselected/
  unfinished/version-mismatch failures, and report the activated version in the
  structured environment and remediation text. An invalid explicit `IDF_PATH`
  fails; it must not silently fall through to EIM.
- **T003:** Add the migration invariant test first, activate the EIM 6.1.1
  environment, build in a truly empty out-of-tree directory, and resolve each
  missing v6 component at the direct consumer. Regenerate configuration and
  lock state only with 6.1.1. Compare named settings against T001 and explain
  every changed or removed Kconfig symbol; do not copy obsolete values back.
- **T004:** Make the exact baseline durable in tests and docs. Search project
  files for 5.5 references with exclusions for Git history, ignored evidence,
  and the US-006 migration history where mentioning 5.5 is intentional. Review
  protocol, heartbeat, UART pin, partition, and ownership diffs explicitly.
- **T005:** Run all real host checks and retain raw output. Classify an absent
  tool/environment as blocked and a compile/configuration regression as failed.
  Neither outcome allows T006 or cleanup.
- **T006:** Add `US006-PROC-001` under the shared verification procedures. It
  defines exact device resolution, isolation, deterministic repetition counts,
  network/client setup, controller-neutral checks, evidence filenames, secret
  redaction, and the rule that failed or inconclusive checks preserve 5.5.
- **T007:** Pause for the connected exact device and Gate 1 approval. Flash
  only that port. Capture three cold/USB boots, three software resets, and three
  Wi-Fi loss/recovery cycles. Record failures rather than repairing or deleting
  5.5 in the same step.
- **T008:** Start two independent `websocat` clients, produce at least ten
  identifiable Pico UART log lines, verify both receive them, then disconnect
  each client in turn and prove the survivor continues. Retain independent
  timestamped captures.
- **T009:** Pair once and perform three controller disconnect/reconnect cycles.
  With neutral steady input, record Pico receiver status before and after a
  30-second interval; frames must advance and freshness must not become stale.
  Exercise a non-motion controller state change with traction power disabled to
  prove the snapshot path. Correlate this with the unchanged source constant and
  frame layout.
- **T010:** Start from a new Git status. Compare the exact legacy
  `components/btstack` tree to the vendored project tree and top-level
  `hello_world` to the checkout's tracked upstream example. Inventory all
  outside-workspace targets without deletion, activate 6.1.1, retain
  `idf_tools.py uninstall --dry-run`, and create an absolute cleanup manifest.
- **T011:** Copy `~/.espressif/tools/eim_idf.json` into ignored `temp/us006/`,
  hash the backup, revalidate every manifest path and prerequisite, then present
  the exact list for explicit owner approval. Remove only approved 5.5 targets
  and the reviewed unused tools/archives. Any drift aborts without broadening
  the manifest.
- **T012:** Re-run EIM selection, doctor, unit/invariant tests, scoped project
  and shell-reference searches, and a second empty-directory build. Promote the
  append-only evidence bundle, commit platform changes in the ESP32 repository,
  and update the parent pointer/docs to the tested child revision. Completion
  review checks every AC; it does not reuse T005 build output as post-cleanup
  proof.

## Physical Gates

**Gate 1 — exact-device flash:** T007 pauses until passive discovery resolves
exactly one stable serial identity, the owner confirms that identity and port,
and explicitly approves flashing the 6.1.1 image. USB device-node coincidence
alone is insufficient.

**Isolated-bench continuation:** T007 through T009 require traction and
motor-driver power physically disabled. Only logic/USB power is permitted. The
existing debug and controller UART harness may be used but not rewired. Stop
for ambiguity, unexpected motion, heat/odor, brownout/reset loops, changed
wiring, or any failed/inconclusive check. No Gate 2, actuator, or motion work is
authorized by this story.

**Destructive Gate D1 — outside-workspace cleanup:** T011 pauses after the
backup, audit, successful device bundle, dry-run review, and exact absolute
manifest exist. The owner must approve that list explicitly. Approval does not
extend to newly discovered paths. Unique or unexplained content, target drift,
or a missing backup aborts cleanup and preserves 5.5.

## Traceability

| Acceptance | Tasks | Evidence |
| --- | --- | --- |
| AC-001 | T003, T005 | Empty-directory configuration and build output before cleanup. |
| AC-002 | T003, T005 | Component declaration diff and successful v6 build. |
| AC-003 | T001, T003, T004, T005 | Named sdkconfig invariant matrix and generated config review. |
| AC-004 | T003, T004, T005 | Lock schema/identity assertion and tracked lock file. |
| AC-005 | T002, T004, T005 | Adapter unit tests plus real adapter/parent doctor results. |
| AC-006 | T001, T004, T005 | Documentation diff, 6.1.1 search, and interface/ownership review. |
| AC-007 | T006, T007, T008, T009 | Exact-device record, Gate 1 approval, isolation checklist, and procedure logs. |
| AC-008 | T006, T007 | Flash, repeated boot/reset serial captures, and Wi-Fi recovery observations. |
| AC-009 | T006, T008 | Two independent WebSocket captures and named Pico UART lines. |
| AC-010 | T006, T009 | Pair/reconnect logs, Pico receiver status deltas, freshness result, and static 100 ms/frame review. |
| AC-011 | T001, T002, T003, T005, T006, T007, T008, T009, T010 | Gated DAG and retained failure/inconclusive results showing cleanup never ran early. |
| AC-012 | T010 | Fresh Git status and complete directory comparison output. |
| AC-013 | T011 | Backup/hash, exact approved manifest, registry/tool cleanup record. |
| AC-014 | T010, T011 | Retained 6.1.1 dry-run and approved subset actually removed. |
| AC-015 | T012 | Selected EIM record, scoped reference search, doctors, tests, second clean build, evidence ID, and integrated Git identities. |

## Plan Change Log

- **v1 (2026-11-19):** Initial implementation plan. Corrected the story's
  ESP32 identity question link to `Q-US002-004`, separated host/device/cleanup
  evidence, defined the adapter and generated-state TDD seams, bounded the
  heartbeat claim to available evidence, and made outside-workspace deletion a
  distinct approval gate.
