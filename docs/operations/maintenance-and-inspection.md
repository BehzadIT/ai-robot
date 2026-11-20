# Maintenance And Inspection

## Purpose
Define the recurring inspection points that keep the robot trustworthy between work sessions.

## Current status
- `Documentation procedure`: derived from the current robot architecture and known weak points.

## Inspection points
- track and sprocket alignment
- shaft adapter tightness and repeatable seating
- motor mount fasteners and clearance
- encoder cable strain relief
- battery pack physical condition
- charger and BMS connector condition
- common-ground integrity

## Notes
Mechanical and electrical degradation can look like firmware issues. Inspection should happen before deeper debugging when behavior changes unexpectedly.

## Sources
- Source file: [faulty-shaft-and-solution.txt](../assets/mechanical/faulty-shaft-and-solution.txt)
- Manual/source file: [DALY smart active-balance BMS manual](../assets/components/power/daly-bms/vendor/daly-smart-active-balance-bms-manual-2024-11-15.pdf)
