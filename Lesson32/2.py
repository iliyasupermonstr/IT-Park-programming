import sys
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication

class Communicate(QObject):
    close_app = pyqtSignal()

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.comm = Communicate()
        self.comm.close_app.connect(self.close)
        self.setGeometry(300,300,290,150)
        self.show()

    def mousePressEvent(self,event):
        self.comm.close_app.emit()
      
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
