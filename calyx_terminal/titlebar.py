from __future__ import annotations

from PySide6.QtCore import QPoint, Qt
from PySide6.QtGui import QMouseEvent
from PySide6.QtWidgets import QFrame, QHBoxLayout, QLabel, QPushButton, QWidget

from . import __version__


class TitleBar(QFrame):
    def __init__(self, window: QWidget) -> None:
        super().__init__(window)
        self.window = window
        self.drag_position: QPoint | None = None
        self.setObjectName("TitleBar")
        self.setFixedHeight(38)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(12, 0, 5, 0)
        layout.setSpacing(2)

        self.logo = QLabel("●")
        self.logo.setObjectName("TitleLogo")
        self.title = QLabel("Calyx Terminal")
        self.title.setObjectName("TitleLabel")
        layout.addWidget(self.logo)
        layout.addSpacing(5)
        layout.addWidget(self.title)
        layout.addStretch(1)

        self.quote_label = QLabel(f"Calyx Labs' Open Source Terminal - Version {__version__}")
        self.quote_label.setObjectName("QuoteLabel")
        layout.addWidget(self.quote_label)
        
        layout.addStretch(1)

        self.minimize_button = self._button("🗕", "Minimize")
        self.maximize_button = self._button("🗖", "Maximize or restore")
        self.close_button = self._button("🗙", "Close")
        self.close_button.setObjectName("CloseButton")
        layout.addWidget(self.minimize_button)
        layout.addWidget(self.maximize_button)
        layout.addWidget(self.close_button)

        self.minimize_button.clicked.connect(window.showMinimized)
        self.maximize_button.clicked.connect(self.toggle_maximized)
        self.close_button.clicked.connect(window.close)

    def _button(self, text: str, tooltip: str) -> QPushButton:
        button = QPushButton(text)
        button.setToolTip(tooltip)
        button.setFixedSize(40, 30)
        button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        from PySide6.QtGui import QCursor, QPixmap
        from pathlib import Path
        cursor_path = Path(__file__).resolve().parent / "assets" / "calyx-cursor.svg"
        button.setCursor(QCursor(QPixmap(str(cursor_path)), 6, 2))
        return button

    def toggle_maximized(self) -> None:
        if self.window.isMaximized():
            self.window.showNormal()
        else:
            self.window.showMaximized()

    def mouseDoubleClickEvent(self, event: QMouseEvent) -> None:
        if event.button() == Qt.MouseButton.LeftButton:
            self.toggle_maximized()
            event.accept()

    def mousePressEvent(self, event: QMouseEvent) -> None:
        if event.button() == Qt.MouseButton.LeftButton:
            self.drag_position = event.globalPosition().toPoint() - self.window.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        if self.drag_position is not None and event.buttons() & Qt.MouseButton.LeftButton:
            if self.window.isMaximized():
                return
            self.window.move(event.globalPosition().toPoint() - self.drag_position)
            event.accept()

    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        self.drag_position = None
        super().mouseReleaseEvent(event)
