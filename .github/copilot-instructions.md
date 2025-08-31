# Copilot Instructions for DeskPod

## Project Overview
DeskPod is a Python application for managing multiple Ubuntu desktop environments (DEs) using LXC containers. It provides a GUI for switching between containerized DEs, ensuring user profile persistence and minimizing dependency conflicts.

## Architecture & Key Components
- **src/main.py**: Entry point for the DeskPod application. Orchestrates GUI and container management.
- **src/gui/**: Contains GUI logic (PyGTK). Handles user interactions for selecting and switching DEs.
- **src/containers/**: Container management logic (LXC commands, lifecycle, mounting home directory).
- **src/config/deskpod_config.json**: Configuration file listing available DEs and their container settings.

## Developer Workflows
- **Container Management**: Use LXC (`lxc-start`, `lxc-stop`, etc.) for lifecycle operations. Containers mount the user's home directory for profile persistence.
- **Configuration**: Add new DEs by updating `deskpod_config.json` with container/image details.
- **GUI Development**: Use PyGTK for all user-facing components. Menu buttons should map to container actions.
- **Testing**: Manual testing is typical; run `python src/main.py` to launch the app and interact with containers.
- **Debugging**: Check LXC logs and container status with `lxc-info` and system logs if issues arise.

## Patterns & Conventions
- **Separation of Concerns**: Keep GUI, container logic, and configuration handling in separate modules.
- **Direct LXC Integration**: Prefer Python subprocess calls to LXC CLI over third-party wrappers for reliability.
- **Profile Persistence**: Always mount the user's home directory into containers; do not copy or sync files.
- **Extensibility**: New DEs should be added via config, not code changes.
- **No Automated Tests Yet**: All validation is manual; document any new test scripts in this file.

## External Dependencies
- **LXC**: Must be installed and configured on the host system.
- **PyGTK**: Required for GUI; list in `requirements.txt`.

## Example Workflow
1. Add a new DE to `deskpod_config.json`.
2. Create/start the container with LXC commands.
3. Use the GUI to switch between DEs.
4. Stop containers via GUI or CLI as needed.

## References
- See `/README.md` for project goals and roadmap.
- See `src/config/deskpod_config.json` for DE/container configuration format.

---
If any section is unclear or missing, please provide feedback for improvement.
