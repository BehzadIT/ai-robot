# Troubleshooting

## Purpose
Provide a fast fault-isolation map for common future debugging sessions.

## Current status
- `Documentation guide`: based on current code, rough notes, and known project conflicts.

## Quick diagnosis map
### Robot does not move
- check battery and driver power
- verify Pico is up and joined to Wi-Fi
- verify command endpoint is reachable
- verify stop state is not latched

### Robot moves badly or noisily
- inspect shaft adapter alignment
- inspect track engagement
- verify encoder feedback is sane
- verify left encoder pin mapping against the current build

### Logs missing on PC
- check Pico UART mirror
- check ESP32 Wi-Fi
- check WebSocket connection to ESP32

### App connects but control is wrong
- verify that Android is connected to the Pico control endpoint, not the ESP32 telemetry bridge
- verify `target_direction` semantics

## Sources
- Source file: [faulty-shaft-and-solution.txt](../assets/mechanical/faulty-shaft-and-solution.txt)
