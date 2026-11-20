# Bringup Procedure

## Purpose
Provide a safe, repeatable high-level bring-up sequence for future work sessions.

## Current status
- `Documentation procedure`: derived from current architecture and electrical constraints.

## Bring-up sequence
1. Inspect wiring, connector seating, and battery condition.
2. Confirm current BMS and pack state before applying power.
3. Bring up the Pico without free-moving tracks first when debugging firmware changes.
4. Confirm Pico Wi-Fi and control endpoint availability.
5. Confirm ESP32 Wi-Fi and WebSocket telemetry path separately.
6. Confirm encoder readings before closed-loop drive testing.
7. Test stop behavior before any sustained motion.

## Notes
Treat command, telemetry, and motor subsystems as separable bring-up targets. Do not assume that one working path proves the others are correct.

## Sources
- Manual/source file: [DALY smart active-balance BMS manual](../assets/components/power/daly-bms/vendor/daly-smart-active-balance-bms-manual-2024-11-15.pdf)
