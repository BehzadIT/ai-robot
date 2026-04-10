# Mechanical Build

## Purpose
Describe the physical robot build at the level needed to inspect, reproduce, and maintain it.

## Current status
- `From vendor documentation`: base chassis is a double-layer suspension crawler.
- `Project note`: current build is upgraded beyond the original stock motor/controller configuration.
- `Needs verification`: exact as-built dimensions after motor and chassis modifications.

## Build summary
- Base: aluminum tracked crawler chassis.
- Drive upgrade: Pololu 37D motors replace the older 520/45:1 references.
- Driver upgrade: Cytron MDD10A replaces stock controller assumptions.
- Chassis may require width expansion and revised motor mounting geometry to fit the current drivetrain reliably.

## Assembly considerations
- Keep track alignment and sprocket engagement as first-class mechanical quality targets.
- Preserve serviceability for motor removal, encoder cable routing, and battery access.
- Treat custom brackets, washers, and shaft adapters as versioned build artifacts, not incidental workshop details.

## Sources
- Manual/source file: [robot_project_components_UPDATED (1).pdf](../../robot-pico-platform/docs/robot_project_components_UPDATED%20%281%29.pdf)
- Manual/source file: [Technical parameters related to suspended tracked vehicles.pdf](../../robot-pico-platform/docs/Technical%20parameters%20related%20to%20suspended%20tracked%20vehicles.pdf)
- Source file: [robot_chassis_expansion_design.txt](../../robot-pico-platform/docs/robot_chassis_expansion_design.txt)
