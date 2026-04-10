# Known Issues And Open Questions

## Purpose
Collect every conflict, missing fact, and unresolved assumption that future engineering work must not ignore.

## Current status
- `High priority`: several project facts are currently inconsistent across code, notes, and vendor material.

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

### Current architecture versus intended architecture
- Intended subsystem split says ESP32 is passive telemetry-only.
- Current code shows the Pico itself exposing the live control WebSocket and HTTP endpoints.
- Impact: future work must not assume command arbitration happens on the ESP32.

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
- Code: [robot_drive_controller.py](../../robot-pico-platform/services/robot_drive_controller.py)
- Code: [robot_cross_coupled_pid.py](../../robot-pico-platform/services/robot_cross_coupled_pid.py)
- Code: [NavigationWebSocketApi.kt](../../robot-android-app/app/src/main/java/com/bizi/roboapp/core/transport/NavigationWebSocketApi.kt)
- Source file: [wiring reference.txt](../../robot-pico-platform/docs/wiring%20reference.txt)
- Source file: [Robot battery system.txt](../../robot-pico-platform/docs/Robot%20battery%20system.txt)
- Source file: [Pololu_37D_Encoder_Spec_and_RPM_Test_Code (1).txt](../../robot-pico-platform/docs/Pololu_37D_Encoder_Spec_and_RPM_Test_Code%20%281%29.txt)
- Manual/source file: [Smart Active Balance BMS manual.pdf](../../robot-pico-platform/docs/Smart%20Active%20Balance%20BMS%20manual.pdf)
- Manual/source file: [EXHAUSTIVELY_COMPLETE_Robot_Project_Component_List.txt](../../robot-pico-platform/docs/EXHAUSTIVELY_COMPLETE_Robot_Project_Component_List.txt)
