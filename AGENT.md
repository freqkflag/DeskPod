# 🤖 DeskPod Agents

This document describes the agents, scripts, and automation processes used to build, test, and manage the **DeskPod** project. Each agent has a defined role, scope, and interface.

---

## 📦 Container Agents

### **LXC Manager Agent**

* **Role:** Manage lifecycle of containerized desktop environments.
* **Tasks:**

  * Start/stop DE containers (`lxc-start`, `lxc-stop`).
  * Mount `$HOME` into containers.
  * Apply networking and GPU passthrough settings.
* **Interface:**

  * YAML config (`config/desktops.yaml`).
  * Python subprocess calls.

### **Container Builder Agent**

* **Role:** Automate creation of base containers for each DE.
* **Tasks:**

  * Initialize base Ubuntu image (`lxc-create`).
  * Install DE packages (GNOME, KDE, XFCE, Deepin, etc.).
  * Configure session display method (X11, VNC).
* **Interface:**

  * Build scripts under `scripts/build-*.sh`.
  * Reads global config.

---

## 🖥️ GUI Agents

### **Switcher Agent (PyGTK)**

* **Role:** Provide graphical interface to switch desktops.
* **Tasks:**

  * Render menu of available DEs from YAML config.
  * Handle button clicks → invoke LXC Manager Agent.
  * Display container session status.
* **Interface:**

  * Runs as `deskpod.py`.
  * Reads from `config/desktops.yaml`.

### **Session Display Agent**

* **Role:** Manage how containerized DE is shown on host screen.
* **Tasks:**

  * Configure X11 socket sharing OR
  * Launch/manage VNC server in container.
* **Interface:**

  * Called by Switcher Agent.
  * Configurable via YAML (`display: x11|vnc`).

---

## 🛠️ Build & CI Agents

### **Lint & Test Agent**

* **Role:** Validate DeskPod source code and configs.
* **Tasks:**

  * Lint Python (`flake8`).
  * Validate YAML configs.
  * Run basic container launch tests in CI.
* **Interface:**

  * GitHub Actions / GitLab CI jobs.

### **Packaging Agent**

* **Role:** Package DeskPod for easy installation.
* **Tasks:**

  * Build `.deb` package.
  * Create Snap manifest.
  * Generate `.desktop` launcher file.
* **Interface:**

  * CI/CD pipelines.
  * Outputs published artifacts.

---

## 🔑 Future Agents

* **Telemetry Agent:** Collect optional metrics about DE switching.
* **Secrets Agent:** Inject credentials (Vault/Infisical) into containers.
* **AI Dev Agent:** Automate documentation updates & generate test scaffolds.

---

## 🗂️ File Locations

* `config/desktops.yaml` → Defines available DEs.
* `scripts/*.sh` → Container build & lifecycle scripts.
* `src/deskpod.py` → GUI Switcher Agent.
* `.github/workflows/*.yml` → CI/CD Agents.

---
