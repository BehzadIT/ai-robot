# Glossary

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
