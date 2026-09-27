from __future__ import annotations

import sys
from pathlib import Path

from PySide6.QtCore import Qt
from PySide6.QtGui import QAction, QGuiApplication, QIcon, QKeySequence
from PySide6.QtWidgets import QApplication, QMainWindow, QMenu, QStatusBar, QVBoxLayout, QWidget

from .config import Config
from .terminal_widget import TerminalWidget
from .theme import APP_STYLE
from .titlebar import TitleBar


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.config = Config()
        self.setWindowTitle("Calyx Terminal")
        self.setObjectName("CalyxTerminalWindow")
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.Window)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, False)

        icon_path = Path(__file__).resolve().parent / "assets" / "calyx-terminal.png"
        self.setWindowIcon(QIcon(str(icon_path)))

        root = QWidget(self)
        root.setObjectName("RootWidget")
        layout = QVBoxLayout(root)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        self.title_bar = TitleBar(self)
        self.terminal = TerminalWidget(self.config, self)
        layout.addWidget(self.title_bar)
        layout.addWidget(self.terminal, 1)
        self.setCentralWidget(root)

        status = QStatusBar(self)
        status.setSizeGripEnabled(True)
        status.showMessage("Calyx Terminal  •  Ctrl+Shift+C/V to copy/paste")
        self.setStatusBar(status)
        self._create_actions()
        self.resize(1050, 700)
        self.setMinimumSize(640, 400)

    def _create_actions(self) -> None:
        self.copy_action = QAction("Copy", self)
        self.copy_action.setShortcut(QKeySequence("Ctrl+Shift+C"))
        self.copy_action.triggered.connect(self.terminal.copy_selected)
        self.paste_action = QAction("Paste", self)
        self.paste_action.setShortcut(QKeySequence("Ctrl+Shift+V"))
        self.paste_action.triggered.connect(self.terminal.paste_text)
        self.clear_action = QAction("Clear scrollback", self)
        self.clear_action.setShortcut(QKeySequence("Ctrl+Shift+L"))
        self.clear_action.triggered.connect(self.terminal.clear)
        self.zoom_in_action = QAction("Zoom in", self)
        self.zoom_in_action.setShortcut(QKeySequence("Ctrl++"))
        self.zoom_in_action.triggered.connect(self.terminal.zoomIn)
        self.zoom_out_action = QAction("Zoom out", self)
        self.zoom_out_action.setShortcut(QKeySequence("Ctrl+-"))
        self.zoom_out_action.triggered.connect(self.terminal.zoomOut)
        self.addActions([self.copy_action, self.paste_action, self.clear_action, self.zoom_in_action, self.zoom_out_action])

    def contextMenuEvent(self, event) -> None:
        menu = QMenu(self)
        menu.addAction(self.copy_action)
        menu.addAction(self.paste_action)
        menu.addSeparator()
        menu.addAction(self.clear_action)
        menu.addSeparator()
        menu.addAction(self.zoom_in_action)
        menu.addAction(self.zoom_out_action)
        menu.exec(event.globalPos())


def run() -> int:
    QApplication.setApplicationName("Calyx Terminal")
    QApplication.setOrganizationName("Calyx")
    QGuiApplication.setDesktopFileName("calyx-terminal")
    app = QApplication(sys.argv)
    app.setApplicationDisplayName("Calyx Terminal")
    app.setStyle("Fusion")
    app.setStyleSheet(APP_STYLE)
    icon_path = Path(__file__).resolve().parent / "assets" / "calyx-terminal.png"
    app.setWindowIcon(QIcon(str(icon_path)))
    window = MainWindow()
    window.show()
    return app.exec()
