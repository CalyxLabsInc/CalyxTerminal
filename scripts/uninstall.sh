#!/usr/bin/env bash
set -euo pipefail
rm -rf "$HOME/.local/share/calyx-terminal"
rm -f "$HOME/.local/bin/calyx-terminal"
rm -f "$HOME/.local/share/applications/calyx-terminal.desktop"
rm -f "$HOME/.local/share/icons/hicolor/scalable/apps/calyx-terminal.svg"
rm -f "$HOME/.local/share/icons/hicolor/256x256/apps/calyx-terminal.png"
command -v update-desktop-database >/dev/null 2>&1 && update-desktop-database "$HOME/.local/share/applications" || true
printf 'Calyx Terminal uninstalled. Configuration in ~/.config/calyx-terminal was retained.
'
