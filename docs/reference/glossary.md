# Glossary

## Claim And Planning States

Use these states for meaningful claims in canonical documentation. A claim may
move between states only when the reason and supporting source or observation
are recorded.

| State | Meaning |
| --- | --- |
| `Bench verified` | Confirmed on the physical system with retained observations or evidence |
| `Software verified` | Confirmed by an automated or repeatable software check, but not necessarily on hardware |
| `Owner reported` | Supplied by the owner and useful, but not independently verified |
| `Documented / unverified` | Present in a project source but not reconciled with code or hardware |
| `Implemented` | Exists in code; runtime or physical qualification may still be outstanding |
| `Planned` | Approved target direction, not current behavior |
| `Explore` | A possibility retained without architectural commitment |
| `Conflicting` | Two or more credible sources disagree |
| `Suspected missing` | Evidence suggests a fact or component exists, but canonical context omits it |
| `Unknown` | Required information has not been established |

These claim states are distinct from backlog lifecycle states such as
`Draft`, `Ready`, `In Progress`, and `Done`. Refinement and verification are
activities rather than separate backlog states.

## BMS
Battery Management System. Handles pack protection and, depending on model, balancing and communication.

## CPR
Counts per revolution. In this project, the Pololu note treats `64 CPR` as fully decoded quadrature counts at the motor shaft.

## Cytron MDD10A
Dual-channel DC motor driver used for current robot motor control.

## PIO
Programmable I/O on the RP2040, used here for efficient quadrature encoder counting.

## REPL
Read-eval-print loop. The Pico USB console behavior must remain compatible with normal tooling.

## Stale-command stop
A control safety behavior where old or missing commands should lead to a stop state.

## UART mirror
The Pico logging behavior that copies `print()` output to UART while preserving normal USB output.
