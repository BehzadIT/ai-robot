# Electrical Design Source

The logical KiCad project will live here as `robot-system.kicad_pro` and
`robot-system.kicad_sch`. It must describe intended rails, protection, nets,
connectors, voltage domains, and component values without claiming to be the
as-built robot.

Creation is currently blocked by two explicit prerequisites:

- KiCad is not installed in the inspected development environment.
- `Q-US002-001`, `Q-US002-004` through `Q-US002-007`, `Q-US002-016`, and
  `Q-US002-018` leave safety-relevant device/connector details unresolved.

Unknown facts must appear as unresolved question references, not guessed
symbols or values. Installing KiCad requires owner authorization. Record the
selected KiCad version when the project is first created.
