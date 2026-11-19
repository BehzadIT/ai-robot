# Capability Roadmap

## Purpose

Describe capability direction without presenting estimates or exploratory ideas
as implemented architecture. Horizons express dependency order, not calendar
commitments.

## Now: Reliable Control Foundation

- Complete the reliable Pico C++ no-network runtime baseline.
- Stabilize the ESP32 gateway shape without transferring safety authority.
- Resolve control-critical hardware identity and wiring conflicts.
- Apply lightweight risk classification, evidence expectations, and backlog
  traceability during migration work.
- Establish the component/evidence and toolchain contracts in US-002 and
  US-003 without pulling them into US-001.

## Next: Integrated And Observable Teleoperation

- Add bounded and validated ESP32-to-Pico command transport.
- Restore drivetrain, encoder, watchdog, stop, and recover parity in safe
  slices.
- Route Android operator intent through ESP32.
- Add structured gateway and Pico control diagnostics.
- Qualify disconnect, stale input, malformed command, reconnect, and log
  backpressure behavior.

## Later: Reproducible Sensing And Platform Capabilities

- Admit sensors only after exact variants, electrical interfaces, mounting,
  calibration, and failure behavior are documented.
- Record reproducible integrated releases containing software, hardware,
  calibration, and verification identities.
- Add richer replay, simulation, hardware-in-the-loop, and maintenance
  diagnostics.
- Establish data-capture and perception foundations without coupling them
  directly to actuator authority.

## Explore: Autonomy And Physical AI

- Obstacle avoidance, mapping, localization, and autonomous navigation.
- Edge inference and perception-assisted operator control.
- Dataset capture, simulation-to-real workflows, and learned policies.
- Additional mechanical capabilities or manipulation.

`Explore` is not an architectural commitment. Any future autonomy may propose
bounded operator-like intent, but Pico retains freshness, admission, manual
override, fault handling, and final motion authority unless an explicit safety
review changes the system architecture.

## Open Roadmap Decisions

These questions affect prioritization, not the current ownership boundary.
They should be answered from owner intent rather than inferred from inventory.

| ID | Known context | Decision needed | Why it matters | Preferred input | Status |
| --- | --- | --- | --- | --- | --- |
| `Q-US001-001` | Reliable teleoperation and the clean gateway/control split come first; the inventory mentions several sensors but does not commit them to integration | Rank the desired outcomes after reliable teleoperation: obstacle avoidance, mapping/localization, autonomous navigation, perception/edge AI, manipulation, or another capability | Prevents every available sensor from becoming an accidental commitment | Ranked goals and important use cases | `Open` |
| `Q-US001-002` | The robot is currently a solo-developed learning and experimentation platform with possible future AI/robotics growth | Decide whether it is primarily a long-running learning platform, a future product/research platform, or both | Changes acceptable process weight, modularity, reproducibility, and hardware investment | Owner description | `Open` |
| `Q-US001-003` | The current docs establish a tracked chassis and bench work but not a qualified operating envelope | Identify intended environments such as indoor bench/floor, outdoor terrain, or remote operation | Affects chassis, sensing, ingress protection, communications, and safety decisions | Environments and constraints | `Open` |
| `Q-US001-004` | Pico Wi-Fi fragility is already treated as a migration constraint, while other hardware and tooling choices may also be temporary | Identify present constraints that are temporary compromises rather than long-term strategy | Prevents migration artifacts and spare parts from shaping the permanent architecture | List of temporary compromises | `Open` |

Unknown answers block only the capabilities that depend on them. They do not
block reliable-control, documentation, or independent verification work.

## Related Docs

- System architecture: `system-architecture.md`
- Backlog contract: `../backlog/workflow.md`
- Clean-start plan:
  `../operations/esp32-gateway-pico-control-clean-start-plan.md`
