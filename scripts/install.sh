#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
INSTALL_ROOT="$HOME/.local/share/calyx-terminal"
VENV="$INSTALL_ROOT/venv"

command -v python3 >/dev/null || { echo "Error: python3 is required." >&2; exit 1; }
python3 -m venv "$VENV"
"$VENV/bin/python" -m pip install --upgrade pip setuptools wheel
"$VENV/bin/python" -m pip install "$ROOT"

mkdir -p "$HOME/.local/bin"          "$HOME/.local/share/applications"          "$HOME/.local/share/icons/hicolor/scalable/apps"          "$HOME/.local/share/icons/hicolor/256x256/apps"
ln -sfn "$VENV/bin/calyx-terminal" "$HOME/.local/bin/calyx-terminal"
install -m 0644 "$ROOT/desktop/calyx-terminal.desktop" "$HOME/.local/share/applications/calyx-terminal.desktop"
install -m 0644 "$ROOT/calyx_terminal/assets/calyx-terminal.svg" "$HOME/.local/share/icons/hicolor/scalable/apps/calyx-terminal.svg"
install -m 0644 "$ROOT/calyx_terminal/assets/calyx-terminal-256.png" "$HOME/.local/share/icons/hicolor/256x256/apps/calyx-terminal.png"

command -v update-desktop-database >/dev/null 2>&1 && update-desktop-database "$HOME/.local/share/applications" || true
command -v gtk-update-icon-cache >/dev/null 2>&1 && gtk-update-icon-cache -f -t "$HOME/.local/share/icons/hicolor" || true

printf '
Calyx Terminal 1.0.0 installed successfully.
'
printf 'Launch it from the application menu or run: %s
' "$HOME/.local/bin/calyx-terminal"
