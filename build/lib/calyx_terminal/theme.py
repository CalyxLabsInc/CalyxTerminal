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
"""
