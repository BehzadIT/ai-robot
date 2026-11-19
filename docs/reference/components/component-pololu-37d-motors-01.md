# Pololu 37D Drivetrain Motors And Encoders

Registry ID: `component-pololu-37d-motors-01`

Two owner-reported Pololu 37D 30:1 motors drive the tracks and provide
quadrature feedback. Exact order numbers and encoder variants remain unknown.
The current conversion assumes 64 fully decoded counts per motor revolution
and 1,920 per output revolution.

Three facts must be separated:

- the candidate encoder documentation says 3.5-20 V supply;
- the wiring note says the encoders receive Pico 3.3 V;
- current code uses right `GP10/11` and left `GP20/21`, while the wiring note
  says left `GP12/13`.

Do not normalize these conflicts. Use power-isolated continuity for pin mapping
and a powered, approval-gated measurement for supply and signal levels. A
multimeter can establish DC supply and static levels, but not waveform timing
or edge integrity.
