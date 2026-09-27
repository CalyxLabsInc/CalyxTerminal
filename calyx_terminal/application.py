from __future__ import annotations

import sys
from pathlib import Path

from PySide6.QtCore import Qt, QObject, QEvent
from PySide6.QtGui import QAction, QCursor, QGuiApplication, QIcon, QKeySequence, QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow, QMenu, QStatusBar, QTabWidget, QVBoxLayout, QWidget

from .config import Config
from .terminal_widget import TerminalWidget
from .theme import APP_STYLE
from .titlebar import TitleBar


class CursorEventFilter(QObject):
    def __init__(self) -> None:
        super().__init__()
        assets = Path(__file__).resolve().parent / "assets"
        self._custom_arrow = QCursor(QPixmap(str(assets / "calyx-cursor.svg")), 6, 2)
        self._custom_ibeam = QCursor(QPixmap(str(assets / "calyx-ibeam.svg")), 12, 12)

    def eventFilter(self, obj: QObject, event: QEvent) -> bool:
        if event.type() == QEvent.Type.CursorChange:
            if hasattr(obj, "cursor"):
                shape = obj.cursor().shape()
                if shape == Qt.CursorShape.IBeamCursor:
                    obj.setCursor(self._custom_ibeam)
                elif shape in (Qt.CursorShape.ArrowCursor, Qt.CursorShape.PointingHandCursor):
                    obj.setCursor(self._custom_arrow)
        return False


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
        layout.addWidget(self.title_bar)
        
        self.tabs = QTabWidget(self)
        self.tabs.setObjectName("TerminalTabs")
        self.tabs.setTabsClosable(True)
        self.tabs.setMovable(True)
        self.tabs.tabCloseRequested.connect(self.close_tab)
        layout.addWidget(self.tabs, 1)

        self.setCentralWidget(root)

        status = QStatusBar(self)
        status.setSizeGripEnabled(True)
        status.showMessage("Calyx Terminal  •  Ctrl+Shift+C/V/T to copy/paste/new tab")
        self.setStatusBar(status)
        
        cursor_path = Path(__file__).resolve().parent / "assets" / "calyx-cursor.svg"
        custom_cursor = QCursor(QPixmap(str(cursor_path)), 6, 2)
        self.setCursor(custom_cursor)
        self.tabs.setCursor(custom_cursor)
        self.tabs.tabBar().setCursor(custom_cursor)

        self._create_actions()
        self.add_tab()
        
        self.resize(1050, 700)
        self.setMinimumSize(640, 400)

    def current_terminal(self) -> TerminalWidget | None:
        return self.tabs.currentWidget()

    def add_tab(self) -> None:
        term = TerminalWidget(self.config, self)
        index = self.tabs.addTab(term, f"Terminal {self.tabs.count() + 1}")
        self.tabs.setCurrentIndex(index)
        term.setFocus()
        term.finished.connect(lambda: self.close_tab(self.tabs.indexOf(term)))

    def close_tab(self, index: int) -> None:
        if index >= 0:
            widget = self.tabs.widget(index)
            self.tabs.removeTab(index)
            widget.deleteLater()
            if self.tabs.count() == 0:
                self.close()

    def _create_actions(self) -> None:
        self.new_tab_action = QAction("New tab", self)
        self.new_tab_action.setShortcut(QKeySequence("Ctrl+Shift+T"))
        self.new_tab_action.triggered.connect(self.add_tab)
        
        self.copy_action = QAction("Copy", self)
        self.copy_action.setShortcut(QKeySequence("Ctrl+Shift+C"))
        self.copy_action.triggered.connect(lambda: self.current_terminal().copy_selected() if self.current_terminal() else None)
        
        self.paste_action = QAction("Paste", self)
        self.paste_action.setShortcut(QKeySequence("Ctrl+Shift+V"))
        self.paste_action.triggered.connect(lambda: self.current_terminal().paste_text() if self.current_terminal() else None)
        
        self.clear_action = QAction("Clear scrollback", self)
        self.clear_action.setShortcut(QKeySequence("Ctrl+Shift+L"))
        self.clear_action.triggered.connect(lambda: self.current_terminal().clear() if self.current_terminal() else None)
        
        self.zoom_in_action = QAction("Zoom in", self)
        self.zoom_in_action.setShortcut(QKeySequence("Ctrl++"))
        self.zoom_in_action.triggered.connect(lambda: self.current_terminal().zoomIn() if self.current_terminal() else None)
        
        self.zoom_out_action = QAction("Zoom out", self)
        self.zoom_out_action.setShortcut(QKeySequence("Ctrl+-"))
        self.zoom_out_action.triggered.connect(lambda: self.current_terminal().zoomOut() if self.current_terminal() else None)
        
        self.addActions([self.new_tab_action, self.copy_action, self.paste_action, self.clear_action, self.zoom_in_action, self.zoom_out_action])

    def contextMenuEvent(self, event) -> None:
        menu = QMenu(self)
        menu.addAction(self.new_tab_action)
        menu.addSeparator()
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
    
    # Install global cursor override filter
    cursor_filter = CursorEventFilter()
    app.installEventFilter(cursor_filter)
    # Store reference so it is not garbage collected
    app._cursor_filter = cursor_filter
    
    app.setApplicationDisplayName("Calyx Terminal")
    app.setStyle("Fusion")
    assets_dir = Path(__file__).resolve().parent / "assets"
    style = APP_STYLE.replace("calyx_terminal/assets", assets_dir.as_posix())
    app.setStyleSheet(style)
    icon_path = Path(__file__).resolve().parent / "assets" / "calyx-terminal.png"
    app.setWindowIcon(QIcon(str(icon_path)))
    window = MainWindow()
    window.show()
    return app.exec()
