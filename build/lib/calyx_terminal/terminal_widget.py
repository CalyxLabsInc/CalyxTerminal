from __future__ import annotations

import os
from pathlib import Path

from PySide6.QtGui import QFont
from pyside6_qtermwidget import QTermWidget


class TerminalWidget(QTermWidget):
    """A real VT-compatible terminal powered by QTermWidget."""

    def __init__(self, config, parent=None) -> None:
        # startnow=0 prevents the shell from starting before all settings exist.
        super().__init__(0, parent)
        self.config = config
        assets = Path(__file__).resolve().parent / "assets"

        self.addCustomColorSchemeDir(str(assets))
        self.setColorScheme("CalyxNeon")
        self.setTerminalOpacity(1.0)
        self.setMargin(10)
        self.setHistorySize(int(config["history_lines"]))
        self.setFlowControlEnabled(True)
        self.setFlowControlWarningEnabled(False)
        self.setBidiEnabled(True)
        self.setDrawLineChars(True)
        self.setConfirmMultilinePaste(True)
        self.setTrimPastedTrailingNewlines(False)

        font = QFont(str(config["font_family"]), int(config["font_size"]))
        font.setStyleHint(QFont.StyleHint.Monospace)
        font.setFixedPitch(True)
        self.setTerminalFont(font)

        shell = str(config["shell"])
        self.setShellProgram(shell)
        if Path(shell).name == "bash":
            self.setArgs(["--noprofile", "--norc", "-i"])

        start_dir = Path(str(config["working_directory"])).expanduser()
        if not start_dir.is_dir():
            start_dir = Path.home()
        self.setWorkingDirectory(str(start_dir))

        # Bash expands \w every time the prompt is drawn, so cd immediately
        # updates the path without exposing username or hostname.
        environment = [f"{key}={value}" for key, value in os.environ.items()]
        environment = [item for item in environment if not item.startswith(("PS1=", "PROMPT_COMMAND=", "TERM=", "COLORTERM="))]
        environment.extend([
            "TERM=xterm-256color",
            "COLORTERM=truecolor",
            "PROMPT_COMMAND=",
            r"PS1=\[\e[38;2;255;20;147m\]Calyx Terminal:$(pwd)> \[\e[0m\]",
        ])
        self.setEnvironment(environment)
        self.startShellProgram()

    def copy_selected(self) -> None:
        self.copyClipboard()

    def paste_text(self) -> None:
        self.pasteClipboard()
