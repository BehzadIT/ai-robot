# AI Robot Development Workspace

## Purpose

The tracked `ai-robot-system.code-workspace` file is the canonical VS Code view
for system-level and cross-platform robot work. It presents the parent
integration repository and each platform submodule as separate workspace roots
while preserving their ownership and Git boundaries.

## Opening the workspace

From the parent repository, either open `ai-robot-system.code-workspace` in VS
Code or run:

```sh
code ai-robot-system.code-workspace
```

The workspace contains four named roots:

- `AI Robot System`: shared docs, integration context, and submodule
  revisions owned by the parent repository.
- `Android Operator App`: operator UI, app state, and client transport.
- `ESP32 Platform`: wireless gateway, controller transport, telemetry, and
  diagnostics.
- `Pico Control Platform`: real-time control, safety, motors, encoders, and
  timing-sensitive hardware interaction.

The three submodule directories are hidden beneath the integration root to
avoid duplicate Explorer and search results. They remain fully available under
their dedicated workspace roots.

## Repository and ownership boundaries

The workspace is a development view, not a merged repository. Source Control
should show the parent repository and each initialized submodule independently.
Commit platform changes inside the relevant submodule. Commit shared docs,
workspace configuration, and intentional submodule revision updates in the
parent repository.

Read the parent `AGENTS.md` and shared docs for system-level work. Also read the
nearest platform `AGENTS.md` before changing a child repository. Do not move
control, safety, transport, or UI ownership merely because all projects are
visible in one editor window.

## Platform tooling

The integrated workspace recommends common C/C++, CMake, ESP-IDF, and Python
extensions, but it does not define shared build, flash, deploy, SDK, serial
port, or device settings. Those workflows depend on the active toolchain and
hardware context and remain owned by each platform repository.

Use Android Studio and the Android repository's Gradle workflow for Android
development. Use the ESP-IDF workflow documented by the ESP32 repository. Use
the Pico repository's documented build and deployment workflow for Pico work.

The existing Pico-only workspace remains appropriate when working from a
standalone Pico clone or when the broader system context is unnecessary.

## Portability

All tracked workspace folder paths are relative to the parent repository. Do
not add absolute clone paths, local SDK locations, credentials, serial device
names, or other machine-specific values to the tracked workspace. Keep such
values in ignored local editor settings or the platform's established local
configuration mechanism.
