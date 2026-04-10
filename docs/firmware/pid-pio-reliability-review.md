# Drivetrain PID / PIO Reliability Review

## Purpose
Preserve the parent-level pointer to the detailed Pico drivetrain reliability
review.

The detailed review belongs to the Pico repository because it is about Pico
control-loop lifetime, MicroPython runtime behavior, PIO encoder ownership, PID
state, and motor-output implementation.

## System-Level Conclusion
The robot should keep Pico as the owner of drivetrain safety and timing. The
next drivetrain reliability work should prioritize:
- single ownership of encoder and motor hardware resources
- deterministic control-loop timing
- explicit PID reset and fault behavior
- protocol plumbing that keeps Android intent separate from Pico control logic
- bench validation before retuning

## Implementation Owner
Detailed review and implementation priorities live in:
- `../../robot-pico-platform/docs/drivetrain-pid-pio-reliability-review.md`

Related parent docs:
- `pico-firmware-architecture.md`
- `motor-control-and-encoders.md`
- `../interfaces/command-protocol.md`
- `../verification/known-issues-and-open-questions.md`
