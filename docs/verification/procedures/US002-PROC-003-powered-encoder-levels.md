# US002-PROC-003: Powered Encoder Supply And Signal Levels

Version: 1

Status: Blocked until exact hardware, unpowered mapping, instrument capability,
safe supply topology, emergency disconnect, and owner approval are recorded.

## Goal

Measure each encoder supply and qualify A/B low/high levels without enabling
motor output.

## Why this is needed

The wiring note's 3.3 V supply conflicts with the candidate encoder's documented
3.5 V minimum, and Pico inputs must not receive unsafe levels.

## Tools and protective equipment

- Qualified multimeter for DC supply.
- Oscilloscope or logic analyzer with known ground reference and voltage-rated
  probes for waveform qualification.
- Current-limited supply only after the power topology is reviewed.
- Eye protection and a reachable verified disconnect.

## Safe setup

Motor power physically disabled, tracks secured, encoder wiring qualified by
`US002-PROC-002`, expected levels derived from exact component documentation,
probe ground topology reviewed, and explicit owner approval recorded.

## Procedure

1. Record supply voltage and polarity at each encoder under the named power
   state.
2. Rotate each output slowly by hand and capture A/B low/high levels and phase
   transitions without commanding motor output.
3. Compare voltage levels against both encoder and Pico requirements.
4. If no waveform instrument is available, record only supply/static levels and
   mark waveform/timing claims inconclusive.

## Expected result and tolerance

Populate exact limits from verified motor/encoder and Pico documentation before
execution. An unknown limit blocks the run.

## Failure indications

Overvoltage, undervoltage relative to an exact minimum, missing transitions,
levels outside Pico limits, heat, odor, unstable supply, or unexpected motion.

## Stop conditions

Remove power immediately for any unsafe level, unexpected motor output, rising
current, heat, odor, wiring movement, or loss of the disconnect path.

## How the result changes the decision

The result resolves or preserves `Q-US002-002`; unsafe or marginal levels
create a hardware-interface change proposal rather than a firmware workaround.

## Evidence to retain

Approval, complete setup identity, instrument IDs, measurement points, raw
captures, expected limits, observed levels, uncertainty, and result.
