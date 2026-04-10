# Mounting Fitment And Adapters

## Purpose
Record the non-obvious mechanical fitment constraints around motor mounting and shaft adapters.

## Current status
- `Project note`: original shaft adapter was misaligned and noisy.
- `From project files`: dedicated safe and unsafe mounting studies exist for Pololu 37D integration.

## Known fitment topics
### Shaft adapter issue
The original wheel adapter converting `6 mm D-shaft -> 8 mm hex` was slightly misaligned and caused noisy track motion and poor sprocket holding.

### Proposed or used workaround
- Use a Pololu adapter with `6 mm D` input and `12 mm hex` output.
- Shorten to match the required length.
- Use a washer stack to recreate the stop-ring function if needed.
- Treat wheel-hex modification as a deliberate build change that must be documented before replication.

### Motor mounting geometry
The project contains a fitment study for Pololu 37D motors on a `2 mm` aluminum chassis. The safe pattern intentionally shifts the bolt pattern to improve shaft-hole clearance.

## Sources
- Source file: [faulty-shaft-and-solution.txt](../assets/mechanical/faulty-shaft-and-solution.txt)
- Image: [37d-safe-mounting-detail.png](../assets/mechanical/37d-safe-mounting-detail.png)
- Image: [37d-unsafe-mounting-detail.png](../assets/mechanical/37d-unsafe-mounting-detail.png)
- Data: [37d-mounting-geometry-data.json](../assets/mechanical/37d-mounting-geometry-data.json)
