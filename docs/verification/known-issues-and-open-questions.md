# Known Issues And Open Questions

## Purpose
Collect every conflict, missing fact, and unresolved assumption that future engineering work must not ignore.

## Current status
- Open hardware facts are dormant until a current story decision depends on
  them. They do not form a global prerequisite; the dependent story activates
  the minimum needed question and updates this record with its evidence.
- `High priority`: several project facts are currently inconsistent across code, notes, and vendor material.
- `High priority`: Pico 2 W / CYW43 Wi-Fi bring-up appears optimization-sensitive on some dual-core FreeRTOS builds, so the firmware now has a diagnostic `-O1` profile until that boundary is proven stable.
- `High priority`: next clean-start C++ control firmware should avoid making
  Pico Wi-Fi/CYW43 a boot dependency; ESP32 wireless gateway routing is the
  preferred repair path unless bench evidence overturns this decision.

## Conflicts
### BMS identity conflict
- Source set A describes a DALY Smart BMS `4S 12V 30A`.
- Source set B describes a DALY Smart Active Balance `R24TK1A-17S100A`, `4-8S`.
- Impact: do not assume a UART protocol, current limit, balancing behavior, or configuration interface until bench-confirmed.

### Encoder supply conflict
- Wiring notes show encoder VCC connected to Pico `3.3 V`.
- Pololu note says encoder supply requirement is `3.5 V - 20 V`, with `5 V` recommended.
- Impact: encoder reliability and logic-level assumptions may differ from current notes.

### Encoder pin conflict
- Wiring notes: left encoder on `GP12/13`.
- Current PIO code path: left encoder on `GP20/21`.
- Impact: firmware changes in this area are unsafe without bench verification.
- Tracked by `Q-US002-003`; use the power-isolated continuity procedure before
  changing code or wiring docs.

### Motor-driver control pin conflict
- Wiring notes label `GP8/GP6` as PWM and `GP9/GP7` as direction.
- Current MicroPython and C++ constants label right PWM/DIR as `GP7/GP6` and
  left PWM/DIR as `GP9/GP8`.
- Impact: firmware or wiring changes can swap PWM and direction semantics or
  channel ownership. Do not infer the mapping with powered motor motion.
- Tracked by `Q-US002-016` and the unpowered continuity procedure.

### Charger behavior and charge-current compatibility
- The project battery note says LiFePO4 trickle mode is disabled.
- The retained iQLoad EVO manual describes monitoring and repeated limited
  charging after the main/saturation phases and lists up to 5 A at 12 V.
- The candidate installed-cell datasheet lists 1.1 A maximum charge per cell;
  exact installed cells remain unverified.
- Impact: powered charging qualification remains blocked until exact charger,
  cells, pack construction, BMS, protection, selected program, and allowable
  current are established.
- Tracked by `Q-US002-007`, `Q-US002-017`, and `Q-US002-018`.

### Current architecture versus target gateway architecture
- Older subsystem notes described ESP32 as a passive telemetry bridge.
- Current code shows the Pico itself exposing the live control WebSocket and HTTP endpoints.
- New target split moves wireless gateway duties to the ESP32 while preserving
  Pico command admission, stale-input stop behavior, and motor authority.
- Impact: future work must distinguish current Pico WebSocket control from the
  planned ESP32 WebSocket-to-Pico-UART gateway path. Do not assume command
  arbitration or safety decisions happen on the ESP32.

### Pico 2 W CYW43 / FreeRTOS startup fragility
- Bench investigation found that basic Pico USB CDC, UF2 flashing, project
  CMake, and basic FreeRTOS work, while CYW43/lwIP FreeRTOS startup can prevent
  reliable full firmware progress.
- USB-settle probes and deeper traces narrowed the failure area into CYW43/lwIP
  FreeRTOS initialization rather than the bootloader, cable, USB CDC, or basic
  RTOS scheduler.
- Impact: the clean-start Pico C++ control firmware should boot and enumerate
  without CYW43. Robot Wi-Fi/WebSocket responsibilities should move to ESP32
  gateway stages first.

### Current Android app versus intended operator model
- Intended model includes throttle, steering angle, auto-centering turn control, and stale-command stop semantics.
- Current app exposes signed RPM slider plus stop-on-release behavior.
- Impact: operator docs and protocol docs must distinguish implemented behavior from desired behavior.

### Legacy hardware versus current hardware
- Older notes describe 520 motors and `45:1` gearing.
- Current code and newer notes describe Pololu 37D motors and `30:1` gearing.
- Impact: motor constants, current assumptions, and RPM calculations must use the current stack unless explicitly working on legacy hardware.

## Missing information
### Exact installed BMS
Bench identification needed from the actual hardware label and wiring.

### Exact as-built encoder wiring
Bench continuity check and live signal confirmation needed.

### Exact encoder supply on the current robot
Direct measurement required; do not infer from notes alone.

### Full sensor integration status
The parts inventory includes multiple sensors, but the current control-critical code does not yet document them as active runtime dependencies.

## Working rule
If a statement appears only in rough project notes and cannot be confirmed by code, manual, image, or bench evidence, treat it as `Project note` or `Needs verification`, not as a final fact.

## Sources
- Source file: [wiring-reference.txt](../assets/electrical/wiring-reference.txt)
- Source file: [robot-battery-system.txt](../assets/electrical/robot-battery-system.txt)
- Source file: [pololu-37d-encoder-spec-and-rpm-test-code.txt](../assets/reference/pololu-37d-encoder-spec-and-rpm-test-code.txt)
- Manual/source file: [DALY smart active-balance BMS manual](../assets/components/power/daly-bms/vendor/daly-smart-active-balance-bms-manual-2024-11-15.pdf)
- Manual/source file: [robot-project-complete-component-list.txt](../assets/reference/robot-project-complete-component-list.txt)
