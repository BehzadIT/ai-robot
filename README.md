# AI Robot

This repository is the integration workspace for the AI robot system.

It combines shared system documentation with three independently versioned
platform repositories:

- `robot-android-app`: Android operator app.
- `robot-esp32-platform`: ESP32 platform firmware.
- `robot-pico-platform`: Pico firmware and real-time control.

The platform repositories are included as Git submodules. They keep their own
Git histories, release cycles, and platform-specific instructions. The parent
repository owns shared context, architecture documentation, and the selected
submodule revisions for an integrated robot workspace.

## Clone

Clone with submodules:

```sh
git clone --recurse-submodules <ai-robot-repo-url>
```

If the repository was cloned without submodules:

```sh
git submodule update --init --recursive
```

## Shared Context

Start with:

- `AGENTS.md`
- `docs/README.md`
- `docs/overview/project-summary.md`
- `docs/overview/current-architecture.md`
- `docs/reference/source-index.md`

For platform-specific work, read the `AGENTS.md` inside the target submodule.
Detailed platform implementation docs live in each child repo's `docs/`
directory.

## Submodule Workflow

Commit platform changes inside the relevant submodule. Commit parent-level docs
or submodule pointer updates in this repository.

When a platform repo moves to a new known-good revision:

```sh
cd robot-esp32-platform
git pull
cd ..
git add robot-esp32-platform
git commit -m "Update ESP32 platform revision"
```

The parent repo should record integrated system states, not every intermediate
platform commit.
