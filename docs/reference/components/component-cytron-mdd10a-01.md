# Cytron MDD10A Motor Driver

Registry ID: `component-cytron-mdd10a-01`

The driver converts Pico PWM/direction outputs into motor power. The documented
family accepts 3.3 V logic and 7-30 V motor supply, but the exact board revision
has not been photographed.

The shared wiring note and both current Pico implementations disagree about
which GPIO is PWM versus direction for each track. Resolve `Q-US002-016` by
continuity from named Pico pins to named Cytron inputs and record which channel
drives each track. Do not energize motors merely to infer the map.
