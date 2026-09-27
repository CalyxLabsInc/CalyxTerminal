# Calyx Terminal

<p align="center">
  <img src="calyx_terminal/assets/calyx-terminal.png" alt="Calyx Terminal Logo" width="128"/>
</p>

<p align="center">
  <strong>A neon-pink, VT-compatible Linux terminal emulator built with PyQt/PySide6.</strong>
</p>

<p align="center">
  <a href="https://github.com/CalyxLabsInc/CalyxTerminal/releases/latest"><img src="https://img.shields.io/github/v/release/CalyxLabsInc/CalyxTerminal?style=flat-square&color=FF1493" alt="Latest Release" /></a>
  <a href="https://github.com/CalyxLabsInc/CalyxTerminal/blob/main/LICENSE"><img src="https://img.shields.io/github/license/CalyxLabsInc/CalyxTerminal?style=flat-square&color=FF1493" alt="License" /></a>
  <img src="https://img.shields.io/badge/python-3.10+-blue.svg?style=flat-square" alt="Python Version" />
</p>

Welcome to the **Calyx Terminal**, the flagship open-source terminal developed by **Calyx Labs Inc**. Calyx Terminal provides correct terminal key handling, UTF-8 rendering, ANSI/VT escape processing, cursor movement, and full-screen terminal application support, wrapped in a beautiful custom neon-pink aesthetic.

## Features

- **Multi-Tab Support**: Open multiple terminal sessions with `Ctrl+Shift+T` in beautifully styled tabs.
- **Neon-Pink Aesthetics**: Custom Qt styles, window title bars, and a dark grey cursor with a neon pink outline.
- **True VT-Compatible Engine**: Powered by `QTermWidget`, providing a flawless experience for full-screen CLI apps like `vim`, `nano`, `htop`, and `tmux`.
- **Dynamic Prompt**: The shell dynamically displays the current working directory.
- **Frameless Window**: Custom drag-to-move title bar with beautifully crafted window controls.

## Install (Release 1.0.0)

Extract the archive and run the installation script:

```bash
chmod +x scripts/install.sh scripts/uninstall.sh
./scripts/install.sh
```

The installer creates a private virtual environment under `~/.local/share/calyx-terminal`, installs all Python dependencies, adds the launcher to `~/.local/share/applications`, and installs the icon into your system icon theme.

Launch **Calyx Terminal** directly from your application menu, or via the command line:

```bash
~/.local/bin/calyx-terminal
```

## Run from source

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 main.py
```

## Configuration

Optional settings are stored in `~/.config/calyx-terminal/config.json`:

```json
{
  "font_family": "JetBrains Mono",
  "font_size": 12,
  "shell": "/bin/bash",
  "history_lines": 10000,
  "working_directory": "~"
}
```

## Shortcuts

- `Ctrl+Shift+T`: Open new tab
- `Ctrl+Shift+C`: Copy selected text
- `Ctrl+Shift+V`: Paste from clipboard
- `Ctrl+C`: Interrupt the foreground process
- `Ctrl+L`: Clear the terminal screen
- `Ctrl+Shift+L`: Clear terminal scrollback
- `Ctrl++` / `Ctrl+-`: Zoom in / Zoom out
- `Up` / `Down`: Shell history
- `Tab`: Auto-completion

## Licensing

Calyx Terminal is distributed under the [GPL-3.0-or-later](LICENSE) license.
