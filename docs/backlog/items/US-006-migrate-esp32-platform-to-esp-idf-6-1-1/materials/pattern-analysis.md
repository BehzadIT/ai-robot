# US-006 Pattern Analysis

## Context Inspected

- ESP32 component CMake declarations, tracked `sdkconfig`, lock file, adapter,
  platform docs, and Git history.
- Parent architecture, interfaces, working contract, verification CLI,
  scenario/evidence schemas, hardware and tool registries, and US-002 questions.
- Live read-only EIM registry version 3.0, selected `v6.1.1` installation, the
  legacy 5.5 checkout status, both legacy Python environments, and constraints
  files.

## Selected Pattern

Use a thin Adapter around SDK discovery and activation:

1. An explicit `IDF_PATH` is authoritative and fails closed if invalid.
2. Without it, read the EIM registry's selected installation.
3. Require a selected, finished entry with a usable activation script/path.
4. Execute the authoritative `idf.py --version` and accept exactly 6.1.1.
5. Report the observed root and version through the existing result schema.

This separates selection policy from process execution and makes both testable
without changing the parent adapter protocol.

At the build boundary, use explicit direct component dependencies. ESP-IDF 6
split drivers expose hidden transitive reliance that 5.5 tolerated. Each source
component should name what it consumes; do not add one broad compatibility
component to silence the graph.

## Alternatives Rejected

- **Support both 5.5 and 6.1.1:** conflicts with the sole-baseline outcome and
  multiplies generated configuration and test states.
- **Keep `/home/behzad/Projects/esp-idf` as a fallback:** bypasses EIM selection,
  can silently activate 5.5, and makes doctor output untrustworthy.
- **Trust the EIM registry name without activation:** proves configuration, not
  the SDK actually executed.
- **Retain aggregate `driver` everywhere:** hides direct ownership and does not
  systematically resolve ESP-IDF 6 split-component failures.
- **Accept build success as qualification:** cannot exercise lwIP, Wi-Fi
  recovery, WebSocket concurrency, UART paths, or Bluetooth reconnect.
- **Delete 5.5 immediately after host success:** removes rollback before the
  device-dependent behavior is qualified.
- **Measure the 100 ms heartbeat with an unregistered analyzer:** no suitable
  timing instrument is registered. Static cadence/frame review plus actual Pico
  receiver progress and freshness is honest evidence; it does not claim edge
  timing precision.

## Tradeoffs

Exact version rejection makes upgrades intentional but requires a story change
for every future baseline. EIM parsing couples the adapter to registry version
3.0, so malformed or future incompatible registry structures must fail with a
clear remediation instead of guessing.

The device procedure uses deterministic repetition counts sufficient to expose
basic recovery regressions without pretending to be endurance testing. Three
cycles are qualification smoke coverage, not a reliability lifetime claim.
