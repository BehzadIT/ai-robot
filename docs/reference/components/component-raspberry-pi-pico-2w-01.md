# Raspberry Pi Pico 2 W Control Board

Registry ID: `component-raspberry-pi-pico-2w-01`

The Pico is the final command-admission, freshness, encoder, drivetrain, motor,
and safety authority. ESP32 and Android may deliver intent but cannot replace
this ownership.

The board identity is owner-reported and consistent with the active build
target. Its exact mounting and the as-built motor/encoder harness are not yet
qualified. Current MicroPython and C++ constants agree with each other but
conflict with the shared wiring note for the left encoder and motor-driver
signals. Resolve `Q-US002-003` and `Q-US002-016` by power-isolated continuity
before changing firmware or canonical wiring.

The historical component list calls the Pico 2 W an RP2040 board. That is a
source error; the Pico 2 W uses RP2350. The source remains retained so the
correction is traceable.
