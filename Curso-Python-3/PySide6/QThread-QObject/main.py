from PySide6.QtWidgets import QApplication,QWidget
from ui_worker import Ui_myWidget
import sys
import time

class MyWidget(QWidget, Ui_myWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.button_1.clicked.connect(self.hardWork1)
        self.button_2.clicked.connect(self.hardWork2)

    def hardWork1(self):
        print("Hard work 1")
        time.sleep(5)
        print("Hard work 1 done")
    def hardWork2(self):
        print("Hard work 2")
        time.sleep(5)
        print("Hard work 2 done")
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    app.exec()