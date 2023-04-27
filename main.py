import sys
from PySide6.QtWidgets import (QApplication)
from display import Display
from main_window import MainWindow
from PySide6.QtGui import QIcon
from variables import WINDOW_ICON_PATH
from info import Info
from styles import setupTheme
from buttons import ButtonsGrid

if __name__ == '__main__':

    # cria aplicação
    app = QApplication(sys.argv)
    setupTheme()
    window = MainWindow()

    # def icon
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Info
    info = Info('Sua conta')
    window.addWidgetToVLayout(info)

    # Display
    display = Display()
    display.setPlaceholderText('Digite algo')
    window.addWidgetToVLayout(display)

    # Grid
    buttonsGrid = ButtonsGrid(display, info, window)
    window.vLayout.addLayout(buttonsGrid)

    # executa tudo
    window.adjustFixedSize()
    window.show()
    app.exec()
