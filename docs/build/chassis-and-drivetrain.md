# Chassis And Drivetrain

## Purpose
Define the current drivetrain stack and separate it from older chassis references.

## Current status
- `Bench-verified / project note`: active drivetrain is Pololu 37D plus Cytron MDD10A.
- `Legacy`: original 520 motor and 45:1 notes remain useful only as historical references.

## Current drivetrain
- 2x Pololu 37D metal gearmotors, 30:1, 12 V.
- Integrated dual-channel quadrature encoders.
- Output shaft encoder resolution target in code: `1920 counts/output rev` derived from `64 CPR * 30`.
- Cytron MDD10A handles PWM and direction control.

## Legacy drivetrain references
Older notes mention:
- 520 encoder DC gear motors.
- 45:1 gear ratio.
- Lower stall current and stock controller constraints.

These legacy values must not silently leak into new motor-control assumptions.

## Sources
- Manual/source file: [Pololu_37D_Encoder_Spec_and_RPM_Test_Code (1).txt](../../robot-pico-platform/docs/Pololu_37D_Encoder_Spec_and_RPM_Test_Code%20%281%29.txt)
- Manual/source file: [EXHAUSTIVELY_COMPLETE_Robot_Project_Component_List.txt](../../robot-pico-platform/docs/EXHAUSTIVELY_COMPLETE_Robot_Project_Component_List.txt)
