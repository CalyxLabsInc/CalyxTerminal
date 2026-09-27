APP_STYLE = r"""
QMainWindow, QWidget#RootWidget {
    background: #07030A;
    color: #FF1493;
}
QFrame#TitleBar {
    background: #100713;
    border-top: 1px solid #5C123D;
    border-left: 1px solid #5C123D;
    border-right: 1px solid #5C123D;
}
QLabel#TitleLogo {
    color: #FF1493;
    font-size: 19px;
}
QLabel#TitleLabel {
    color: #FF1493;
    font-size: 14px;
    font-weight: 700;
}
QLabel#QuoteLabel {
    color: #FF4DB8;
    font-size: 12px;
    font-style: italic;
}
QFrame#TitleBar QPushButton {
    color: #FF4DB8;
    background: transparent;
    border: none;
    font-size: 18px;
}
QFrame#TitleBar QPushButton:hover {
    color: #FFD6EC;
    background: #5C123D;
}
QFrame#TitleBar QPushButton#CloseButton:hover {
    color: white;
    background: #D00063;
}
QStatusBar {
    color: #FF1493;
    background: #0D0511;
    border-top: 1px solid #28102C;
}
QMenu {
    color: #FF4DB8;
    background: #120817;
    border: 1px solid #5C123D;
}
QMenu::item:selected {
    color: #FFD6EC;
    background: #5C123D;
}
QTabWidget::pane {
    border: none;
    background: #07030A;
}
QTabWidget::tab-bar {
    alignment: left;
}
QTabBar {
    background: #07030A;
}
QTabBar::tab {
    background: transparent;
    color: #FF4DB8;
    padding: 8px 16px;
    border: none;
    border-bottom: 2px solid transparent;
    margin-right: 2px;
    font-size: 13px;
}
QTabBar::tab:selected {
    color: #FF1493;
    border-bottom: 2px solid #FF1493;
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #07030A, stop:1 #1A0B22);
}
QTabBar::tab:hover:!selected {
    background: #100713;
    border-bottom: 2px solid #5C123D;
}
QTabBar::close-button {
    image: url(calyx_terminal/assets/tab-close.svg);
    margin-top: 1px;
    margin-right: 2px;
}
QTabBar::close-button:hover {
    image: url(calyx_terminal/assets/tab-close-hover.svg);
}
"""
