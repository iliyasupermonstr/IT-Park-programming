import sys
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtGui import QColor,QFrame
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication,QWidget,QInputDialog,QLineEdit,QColorDialog

class Communicate(QObject):
    close_app = pyqtSignal()

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        colors = QColor(0,0,0)
        btn1 = QPushButton("Dialog", self)
        btn1.move(20, 20)
        btn1.clicked.connect(self.show_dialog)
        self.frm = QFrame(self)
        self.frm.setStyleSheet('QWidhet {background-color: %s}' % colors.name())
        self.frm.setGeometry(130,22,100,100)
        self.le = QLineEdit(self)
        self.le.move(130,22)
        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Input Dialog')
        self.show()

    def show_dialog(self):
        text, ok = QInputDialog.getText(self, "Input Dialog", "Enter your name:")
        if ok:
            self.le.setText(str(text))
      
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
