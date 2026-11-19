# Verification Checklist

## Purpose
Track which core claims about the robot are verified and which still require confirmation.

## Checklist
- Confirm actual installed BMS model (`Q-US002-001`).
- Confirm actual left encoder pins on the current build (`Q-US002-003`).
- Confirm Pico-to-Cytron PWM/DIR continuity and track/channel mapping
  (`Q-US002-016`).
- Confirm actual encoder supply and signal levels (`Q-US002-002`).
- Confirm exact installed cells and pack construction without dismantling the
  pack solely for documentation (`Q-US002-018`).
- Confirm charger identity, LiFePO4 program, maintenance behavior, and safe
  charge-current compatibility (`Q-US002-007`, `Q-US002-017`).
- Confirm fuse/protection and a reachable emergency motor-power disconnect
  (`Q-US002-006`, `Q-US002-019`).
- Confirm current WebSocket command path used during normal operation.
- Confirm stop behavior on command release, disconnect, and stale command conditions.
- Confirm current drivetrain hardware matches Pololu 37D and Cytron assumptions.

## Evidence sources
Use a versioned procedure and a new bundle under `evidence/`. Unpowered identity
and continuity work precedes powered checks. Running firmware behavior and a
vendor manual do not prove the as-built harness by themselves.

## Sources
- Source file: [wiring-reference.txt](../assets/electrical/wiring-reference.txt)
- Manual/source file: [smart-active-balance-bms-manual.pdf](../assets/electrical/smart-active-balance-bms-manual.pdf)
- Live question queue: [US-002.yaml](questions/US-002.yaml)
- Procedure index: [procedures/README.md](procedures/README.md)
