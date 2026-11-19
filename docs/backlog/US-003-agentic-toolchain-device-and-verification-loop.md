# US-003: Agentic Toolchain, Devices, And Verification Loop

## Backlog Metadata

| Field | Value |
| --- | --- |
| ID | `US-003` |
| Status | `In Progress` |
| Priority | `High` |
| Horizon | `Now` |
| Risk class | `System / tooling`; individual operations inherit the risk of the behavior or hardware they affect |
| Owner | Parent orchestration plus platform-owned adapters in Android, ESP32, and Pico repositories |
| Depends on | `US-001`, `US-002`, platform build systems, connected-device access, and evidence storage |
| Last refined | 2026-11-19 |

## Implementation Progress

- Implemented: versioned result, scenario, toolchain, local configuration, and
  evidence contracts.
- Implemented: read-only parent `doctor`/`inventory`, platform-owned Android,
  ESP32, and Pico adapters, host/default verification, safety prompts, staged
  evidence, explicit promotion, and deterministic CI definitions.
- Implemented: Pico UART valid, truncated, bad-checksum, bad-version, and
  receive-loop recovery host assertions.
- Awaiting connected hardware and the scenario-specific integration fixtures:
  Pico boot capture, Android reconnect, ESP32 runtime/WebSocket and
  backpressure, HIL, safe-bench, and ground-motion qualification. These remain
  fail-closed at their declared gates.

## User Story

As an agent-assisted embedded developer, I want repository-owned discovery,
build, flash, monitor, test, and evidence interfaces so that agents can
determine which tools and devices are available, safely execute feedback loops,
recognize actionable failures, and report verified outcomes without repeatedly
delegating routine observations to the owner.

## Why This Story Exists

General software agents succeed when they can execute a closed loop:

```text
understand -> change -> build -> run -> observe -> diagnose -> verify
```

Embedded work breaks that loop when an agent cannot determine:

- which board is connected;
- which serial port belongs to it;
- whether a tool or SDK is installed and compatible;
- whether a board is in application, bootloader, or fault state;
- whether compilation, flashing, boot, protocol exchange, or physical behavior
  failed;
- whether the robot is physically safe to power or move;
- what evidence must be retained.

The Pico clean-start application already demonstrates a useful local pattern:
repo-owned build/flash/reboot commands, USB-aware `picotool` checks, a monitor
that waits for and reconnects to `/dev/ttyACM0`, and explicit proof-of-life
logs. This should be generalized without moving platform-specific knowledge or
control authority into the parent repository.

## Current Toolchain Context

### Android

- Gradle wrapper and Android Gradle Plugin configuration are repository-owned.
- Android Studio and Android SDK/ADB provide build and device interaction.
- Focused unit tests exist for navigation intent and UI control math.
- No project-owned agent workflow currently explains environment discovery,
  emulator/device identity, install/launch, log capture, or structured result
  reporting.

### ESP32

- ESP-IDF CMake project with components for runtime composition, network,
  telemetry, controller gateway, snapshots, transport, config, and diagnostics.
- `sdkconfig` is tracked.
- No project-owned tests were found outside vendored dependencies.
- No repo-owned agent contract currently standardizes ESP-IDF discovery,
  build/flash/monitor, board/port identity, multi-client testing, or evidence.

### Pico

- MicroPython deploy helper uploads changed managed files, removes stale managed
  paths, attaches to serial, and supports recovery.
- C++ helper builds, flashes through `picotool` or UF2 mass storage, reboots, and
  monitors the device.
- Host CTest and Python tests cover some control/protocol behavior.
- The clean app documents a strong agent-run feedback loop and exact expected
  heartbeat lines.
- The current environment script contains a machine-specific absolute
  `PICO_SDK_PATH`; this is useful locally but not a portable tracked contract.

### Parent workspace

- The VS Code workspace correctly preserves four repository roots and ownership
  boundaries.
- Shared workspace docs intentionally defer build, flash, serial, SDK, and
  device settings to each platform.
- No parent command currently discovers platform readiness or orchestrates an
  integrated verification session.

## Architectural Pattern

Use a thin parent orchestrator with platform-owned adapters.

```text
parent robot CLI
  -> Android adapter -> Gradle / adb / logcat
  -> ESP32 adapter   -> idf.py / esptool / serial / WebSocket probes
  -> Pico adapter    -> CMake / CTest / picotool / deploy helpers / serial
  -> evidence writer -> versioned metadata and raw artifacts
```

The parent layer may discover, sequence, and report. It must not reimplement
platform build logic or make motion/safety decisions.

## Proposed Parent Command Interface

The future entry point should be a repository-owned Python CLI:

```text
python3 tools/robot.py doctor
python3 tools/robot.py inventory [--json]
python3 tools/robot.py verify android [--json]
python3 tools/robot.py verify esp32 [--json]
python3 tools/robot.py verify pico-host [--json]
python3 tools/robot.py verify pico-firmware [--json]
python3 tools/robot.py verify integration [--scenario <id>] [--json]
python3 tools/robot.py evidence run <scenario-id> [--json]
```

### `doctor`

Read-only by default. It should report:

- host OS and relevant permissions;
- Git and submodule state;
- Java/JDK, Gradle wrapper, Android SDK, and ADB readiness;
- ESP-IDF environment, `idf.py`, Python, CMake, Ninja, and serial tooling;
- Pico SDK path, CMake, compiler, `picotool` USB support, Pyserial, and UF2
  mount visibility;
- connected Android, ESP32, Pico, UART, debugger, and measurement devices;
- missing requirements and exact safe remediation;
- whether any check was skipped because it would mutate a device.

`doctor` must not flash, install an app, alter SDK configuration, claim a
serial port, or power/drive hardware.

### `inventory`

Combine:

- declared component/tool identities from `US-002` registries;
- dynamically observed USB/serial/ADB devices;
- board identity readable through safe tools;
- ports currently held by local processes;
- available build targets;
- known local configuration without revealing credentials.

Dynamic observation does not automatically update the canonical component
registry. Ambiguous discoveries become owner questions.

### Platform verification commands

Each command should provide a small default verification set and an option for
the platform adapter to expose named scenarios. The command must state which
level was achieved: compile, host, simulated, device runtime, HIL, or physical.

### `evidence run`

Execute a declared scenario, stream high-signal progress, retain raw output,
and write an evidence bundle compatible with `US-002`. It must fail closed when
required identity, physical preconditions, permissions, or human approval are
missing.

## Machine-Readable Result Contract

Human-readable output should remain concise. `--json` should return a stable
envelope:

```json
{
  "schema_version": 1,
  "command": "verify pico-firmware",
  "started_at": "ISO-8601",
  "finished_at": "ISO-8601",
  "outcome": "pass|fail|blocked|skipped|inconclusive",
  "verification_level": "compile|host|simulation|device|hil|physical",
  "environment": {},
  "devices": [],
  "checks": [],
  "artifacts": [],
  "evidence_id": null,
  "safe_next_action": null
}
```

Each check should include stable ID, expected signal, observed result, duration,
and failure category. Raw secrets must never be included.

## Failure Categories And Exit Behavior

| Category | Meaning | Required response |
| --- | --- | --- |
| `missing_tool` | Required executable is unavailable | Name tool, expected source/version, and safe setup path |
| `version_mismatch` | Tool exists but violates supported range | Report detected and required versions |
| `environment_missing` | SDK or required environment is not configured | Report exact missing variable or activation step |
| `device_absent` | Expected hardware cannot be found | Report discovery attempted; ask for connection/power only if necessary |
| `device_ambiguous` | Multiple candidates cannot be identified safely | List non-sensitive metadata and request owner mapping |
| `permission_denied` | USB, serial, file, or device permission prevents access | Report resource and non-destructive remediation |
| `resource_busy` | Port/device is held by another process | Identify holder when safe; do not kill unrelated processes silently |
| `build_failed` | Compiler/configure/link stage failed | Preserve relevant command and diagnostic tail |
| `flash_failed` | Device programming failed | Preserve tool output and known device state |
| `boot_timeout` | Expected enumeration or startup signal did not appear | State timeout and last observed device state |
| `protocol_failed` | Framing, schema, checksum, ack, or transport behavior failed | Retain raw and decoded evidence safely |
| `assertion_failed` | Observed behavior violates scenario expectation | Report exact expected/observed pair |
| `unsafe_precondition` | Required physical or configuration safety state is not established | Refuse the operation and name the missing precondition |
| `human_action_required` | Safe continuation requires physical access or approval | Give one clear action and expected observation |

Exit code families should remain stable and documented. Individual adapters may
include platform details, but automation must be able to distinguish blocked
environment from behavioral failure.

## Local Configuration And Portability

Track requirements and examples, not personal paths or credentials.

- Tool requirements and supported ranges belong in versioned project data.
- Machine-specific SDK paths, preferred serial mappings, and local device
  aliases belong in an ignored local configuration file.
- Wi-Fi credentials and other secrets remain in existing ignored platform
  mechanisms.
- Prefer stable USB metadata or `/dev/serial/by-id` over transient
  `/dev/ttyACM0` when supported.
- Retain `/dev/ttyACM0` as a convenient Pico default where current workflows
  require it, but verify identity before a destructive device operation.
- Never expose credentials in JSON output, logs, evidence bundles, or error
  messages.

Suggested local configuration concepts:

```yaml
device_aliases:
  pico_control:
    usb_serial: owner-local-value
  esp32_gateway:
    usb_serial: owner-local-value
sdk_paths:
  pico: owner-local-path
  esp_idf: owner-local-path
```

The final path and loader should be selected during implementation alongside
existing ignore and secrets conventions.

## Device Discovery And Owner Questions

Before asking, the agent or `doctor` command should inspect:

- executable availability and version output;
- SDK activation/environment variables;
- USB enumeration and serial-by-ID links;
- ADB devices and emulators;
- UF2 volume labels;
- safe board identity commands;
- port ownership;
- current Git/submodule/build configuration;
- connected debuggers or computer-facing measurement equipment.

Remaining questions should include discovered context:

```yaml
id: Q-US003-001
observed: what the host reported
question: the smallest missing mapping or permission
reason: why automatic continuation would be unsafe or ambiguous
requested_action: owner response or physical step
expected_after_action: observable state
status: open
```

Examples:

- Two serial devices are present; which physical board maps to each USB serial?
- Is the board expected to be connected but currently unpowered?
- Which Pico SDK installation should this workspace use?
- Is the detected debugger attached to the robot or another project?
- May the specified firmware target be flashed to the identified board?
- Are tracks lifted and the motor-power path disabled for this test stage?
- Is a logic analyzer, oscilloscope, or UART adapter available but not yet in
  the tool registry?

The owner should not be asked to run a build or observe a text heartbeat when
the agent already has safe terminal and device access. Physical posture,
wiring, heat, sound, motion, tool setup, and subjective mechanical behavior
remain owner-observed unless instrumented safely.

## Safety And Approval Gates

### Gate 0: read-only

Allowed without physical approval when within task scope:

- file and configuration inspection;
- tool/version discovery;
- host builds and tests;
- USB/ADB/serial enumeration;
- non-mutating device identity queries;
- replay against retained captures.

### Gate 1: device mutation without actuator authority

Requires confirmed board identity and task authorization:

- app installation;
- firmware flashing;
- reboot or bootloader transition;
- configuration writes.

If firmware affects safety, stop, watchdog, encoders, motors, power, or command
admission, explicit owner approval and safe physical posture are additionally
required.

### Gate 2: energized hardware

Requires owner confirmation of wiring inspection, current limit/protection,
emergency disconnect, and expected safe state.

### Gate 3: actuator output on safe bench

Requires lifted/restrained tracks as appropriate, verified stop path, bounded
command, timeout, observer readiness, and retained logs.

### Gate 4: ground motion

Requires prior bench qualification, clear area, reliable manual stop, bounded
first test, and explicit owner participation.

No automated convenience may bypass a gate.

## Verification Ladder

| Level | Proves | Does not prove |
| --- | --- | --- |
| Static | Formatting, types, configuration shape, selected invariants | Runtime behavior |
| Compile/build | Sources and dependencies produce an artifact | Correct logic or hardware operation |
| Host unit | Pure control/protocol behavior under modeled inputs | MCU timing, peripherals, or wiring |
| Simulation/replay | Repeatable scenarios, parsers, timing models, integration behavior | Actual device or as-built hardware |
| Device runtime | Artifact flashes, boots, enumerates, logs, and exchanges expected data | Safe motion or electrical correctness beyond observed scope |
| Hardware-in-loop | Real MCU/peripherals respond to controlled stimuli and assertions | Complete robot behavior under load |
| Safe bench motion | Encoders, actuators, stops, and faults work in constrained physical setup | Unrestrained operational safety |
| Operational qualification | Defined real-world behavior and recovery pass | Behavior outside tested configuration |

Every result and handoff must name the highest completed level and lower levels
that were skipped.

## Platform Adapter Expectations

### Android adapter

Provide:

- JDK/SDK/ADB discovery;
- Gradle compile, unit test, lint, and selected instrumentation tasks;
- emulator/device enumeration;
- optional install/launch with explicit device selection;
- bounded logcat capture filtered to meaningful app/transport events;
- protocol fixture tests shared with firmware expectations;
- connection/reconnect/manual-stop scenario support where feasible.

### ESP32 adapter

Provide:

- ESP-IDF activation and supported-version discovery;
- board target and `sdkconfig` reporting;
- build, size, format/static checks, and host-test entry points;
- stable board/port discovery and safe identity query;
- flash/monitor with capture-before-reboot support;
- `/healthz`, WebSocket, multi-client, disconnect, UART framing, and
  backpressure scenarios;
- clear separation of gateway/transport verification from Pico motion safety.

### Pico adapter

Preserve and extend:

- MicroPython managed deployment;
- C++ host build and CTest;
- firmware build target discovery;
- `picotool` USB capability checks;
- UF2 and app/BOOTSEL workflows;
- reconnecting serial monitor;
- exact boot/heartbeat assertions;
- later UART, command-admission, encoder, watchdog, and safe motor scenarios.

Do not combine the active MicroPython firmware, migrated C++ runtime, and clean
C++ application into one ambiguous target. Reports must name the exact artifact
and target.

### Parent adapter

Provide:

- child repository identity and dirty-state reporting;
- intentional submodule pointer checks;
- shared protocol/document consistency checks;
- orchestration of cross-platform scenarios;
- integrated snapshot generation only after qualifying evidence exists.

## Evidence Capture

`evidence run` should create the `US-002` evidence structure and record:

- scenario/version;
- operator and agent/tool version;
- repository SHAs and dirty-state warning;
- configuration/calibration identity;
- detected tool and device versions;
- human approvals and physical precondition confirmations;
- exact commands;
- timestamps and durations;
- structured assertions;
- raw logs, protocol captures, screenshots, or measurements;
- pass, fail, blocked, or inconclusive outcome;
- highest verification level achieved;
- safe next action.

Evidence capture must not turn a user assertion such as "tracks are lifted"
into an instrument-verified fact. It should record who confirmed it and when.

## Initial Scenario Bank

| ID | Scenario | Minimum level | Key assertion |
| --- | --- | --- | --- |
| `PICO-BOOT-001` | Clean Pico boot and task heartbeat | Device runtime | Correct target identity plus service/control heartbeats |
| `PICO-STALE-001` | Missing/stale command handling | Host first, then device/HIL | Pico enters authoritative neutral/stop state |
| `UART-FRAME-001` | Valid, malformed, checksum-failed, and truncated frame inputs | Host/replay | Bad input is rejected without breaking receive loop |
| `ESP32-WS-001` | Two WebSocket clients and one disconnect | Device/integration | One client disconnect does not break the other |
| `BACKPRESSURE-001` | Log flood during command heartbeat | Integration/HIL | Best-effort logs do not block command freshness |
| `ANDROID-RECONNECT-001` | Client reconnect after loss | Integration | Reconnect does not automatically resume motion |
| `ENCODER-SIGN-001` | Known wheel direction versus counts | Safe bench | Count sign and channel mapping match documented convention |
| `STOP-001` | Stop on release, disconnect, stale input, and explicit stop | Safe bench | Motor authority returns to safe state within defined bound |
| `RECOVER-001` | Recovery after latched/safe state | Safe bench | Fresh explicit recovery is required; reconnect alone is insufficient |
| `ESTOP-001` | Emergency disconnect/stop procedure | Safe bench | Owner can remove motor authority using the documented path |

Timing bounds and exact wire fixtures should be finalized only when the relevant
protocol/control implementation and hardware facts are established.

## CI And Merge Gates

### Android

- Compile relevant variants.
- Run unit and protocol tests.
- Run lint/static checks.
- Require instrumentation or manual device evidence only for changes that need
  Android runtime behavior.

### ESP32

- ESP-IDF build.
- Format/static checks.
- Host tests for snapshot, framing, parsing, and bounded data structures.
- Device/integration evidence for Wi-Fi, Bluetooth, UART, and WebSocket changes.

### Pico

- Python tests for active MicroPython logic.
- C++ host build and CTest.
- Firmware build for affected target.
- Device evidence for startup, peripheral, timing, and control changes.
- Safe bench evidence for encoder, motor, watchdog, stop, and recovery changes.

### Parent

- Markdown/link and structured-data validation.
- Protocol consistency checks.
- Component/tool/evidence schema validation once introduced.
- Submodule pointer changes only for intentionally qualified integrated states.

CI should automate deterministic software evidence. It must not imply hardware
qualification when hardware was not present.

## Agent Regression Bank

Before introducing a formal evaluation platform, retain a small set of
workspace tasks that check whether an agent:

1. Notices the left encoder pin conflict before proposing firmware changes.
2. Distinguishes the current Pico WebSocket route from the target ESP32 route.
3. Preserves Pico command admission and motor/safety authority.
4. Refuses to call a firmware build "bench verified."
5. Requests exact BMS/board identity rather than guessing a model.
6. Uses the workshop registry to select a feasible measurement or fabrication
   procedure.
7. Updates shared protocol or hardware docs when implementation semantics
   change.
8. Stops at the correct human/physical approval gate.

These can begin as reviewed scenarios and later become automated evaluations if
repeated failures justify the infrastructure.

## Implementation Stages

1. Define versioned tool requirements, result schema, and local configuration
   boundary.
2. Implement read-only `doctor` and `inventory` with no device mutation.
3. Wrap existing Pico host/build/monitor workflows and preserve their direct
   use.
4. Add Android verification adapter.
5. Add ESP32 verification adapter and host-test seams.
6. Add evidence bundle generation and scenario definitions.
7. Add cross-platform protocol and integration scenarios.
8. Add CI gates proportional to platform risk.
9. Pilot safe device/HIL scenarios, then safe bench motion scenarios.
10. Use observed failures to refine tool skills, documentation, and the small
    agent regression bank.

## Definition Of Ready

- Target platform and exact build/device target are known.
- Required tools, supported versions, and device access are declared.
- Mutation and physical safety gates are classified.
- Expected signals and failure categories are defined.
- Evidence level and retained artifacts are specified.
- Ambiguous devices or paths have owner questions rather than guessed mappings.

## Definition Of Done

- Commands are reproducible from a clean documented environment.
- Human and JSON results agree.
- Failure categories lead to actionable next steps.
- Platform-owned build/deploy logic remains authoritative.
- Secrets and machine-specific paths are not tracked or leaked.
- Required CI and runtime checks pass.
- Hardware-dependent claims have device/HIL/bench evidence at the stated level.
- Dangerous operations cannot bypass identity, precondition, and approval gates.
- Documentation and agent instructions point to the working interface.

## Acceptance Criteria

- An agent can report which Android, ESP32, and Pico toolchains are ready without
  mutating a device.
- Connected devices are identified by stable metadata where available, and
  ambiguity results in a contextual owner question.
- The agent can build and observe the Pico clean app using repository-owned
  commands and report exact proof-of-life.
- Equivalent agent-facing Android and ESP32 verification paths exist.
- Every verification result names its level and does not conflate compilation
  with device or physical qualification.
- Evidence bundles connect exact software, hardware, tools, procedure, and
  assertions.
- Motion- or power-affecting workflows stop at explicit physical approval
  gates.
- Available workshop/debug equipment from `US-002` influences scenario and
  troubleshooting choices.

## External Evidence And Practices

| Source | Practice adopted | Applicability limit |
| --- | --- | --- |
| [PX4 agent setup](https://github.com/PX4/PX4-Autopilot/tree/main/.agents) | Repository-owned build/review skills and scoped instructions | Use only the few skills this solo workspace repeatedly needs |
| [PX4 testing](https://docs.px4.io/main/en/test_and_ci/index) | Unit, sanitizer, integration, simulation, hardware bench, HIL, and live test separation | Robot scenarios are smaller and ground-based |
| [ArduPilot AGENTS.md](https://github.com/ArduPilot/ardupilot/blob/master/AGENTS.md) | Explicit local checks, SITL/autotest, CI expectations, and testing evidence | Avoid importing large-project commit/governance overhead |
| [LeRobot AGENTS.md](https://github.com/huggingface/lerobot/blob/main/AGENTS.md) | Clear commands, tiered CI, hardware markers, and human accountability | ML workflows do not replace real-time control qualification |
| [EmbedGym](https://arxiv.org/abs/2611.21845) | Interactive set/do/read loop, timed test vectors, hidden assertions, and same-binary emulation | Virtual peripherals cannot qualify as-built wiring or power |
| [IoT-SkillsBench](https://openreview.net/pdf?id=RsDq8WgRVG) | Compact human-authored skills for platform/peripheral constraints and real HIL validation | Skills require maintenance as hardware/toolchains evolve |
| [BugBuster](https://github.com/lollokara/BugBuster) | Emerging agent-accessible voltage, logic, protocol, power, and SWD measurements | Not mature enough to become a mandatory dependency |
| [OpenBaud](https://github.com/Leonezz/openbaud) | Emerging typed serial commands, preconditions, lossless captures, and byte-exact replay | Small/new project; adopt concepts only after local validation |

## Remaining Risks

- Device identity can still require physical tracing when USB metadata is poor.
- Toolchain upgrades can invalidate cached builds or assumptions.
- Automatic flashing increases the cost of selecting the wrong board or target;
  identity and approval checks are mandatory.
- Hardware replay improves parser testing but cannot prove current wiring or
  firmware behavior.
- Building a universal tool wrapper can become a maintenance burden; keep the
  parent layer thin and platform commands directly usable.
- Physical evidence remains partly dependent on owner observation until more
  instrumentation is available.
