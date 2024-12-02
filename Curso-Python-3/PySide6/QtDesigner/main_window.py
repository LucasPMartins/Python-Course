import sys
from PySide6.QtCore import QObject,QEvent # type: ignore
from PySide6.QtGui import QKeyEvent # type: ignore
from PySide6.QtWidgets import QApplication, QMainWindow
from window import Ui_MainWindow
from typing import cast

class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.buttonSend.clicked.connect(self.update_label)
        self.lineName.installEventFilter(self)

    def update_label(self):
        text = self.lineName.text()
        self.labelResult.setText(f"Hello, {text}!")

    def eventFilter(self,watched:QObject,event:QEvent) -> bool:
        if event.type() == QEvent.Type.KeyPress:
            event = cast(QKeyEvent,event)
            text = self.lineName.text()
            self.labelResult.setText(f"Hello, {text + event.text()}")
            # print(event.text(),"Key Pressed")
        return super().eventFilter(watched,event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()