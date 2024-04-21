import sys
from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication,QFrame,QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        self.col = QColor(0,0,0)
        redb = QPushButton('Red', self)
        redb.setCheckable(True)
        redb.move(10,10)
        redb.clicked[bool].connect(self.set_color)
        self.col = QColor(0,100,0)
        greenb = QPushButton('Green', self)
        greenb.setCheckable(True)
        greenb.move(10,60)
        greenb.clicked[bool].connect(self.set_color)
        self.col = QColor(0,0,100)
        blueb = QPushButton('Blue', self)
        blueb.setCheckable(True)
        blueb.move(10,110)
        blueb.clicked[bool].connect(self.set_color)

        self.square = QFrame(self)
        self.square.setGeometry(150,20,100,100)
        self.square.setStyleSheet("QWidget { background-color: %s }" %
                                  self.col.name())
        self.setGeometry(600,600,560,340)
        self.setWindowTitle('Toggle button')
        self.show()
    
    def set_color(self,pressed):
        source = self.sender()
        if pressed:
            val = 255
        else: val =0
        
        if source.text() == "Red":
            self.col.setRed(val)
        elif source.text() == "Green":
            self.col.setGreen(val)
        elif source.text() == "Blue":
            self.col.setBlue(val)
        self.square.setStyleSheet("QWidget { background-color: %s }" %
                                  self.col.name())

    def change_title(self, state):
        if state == Qt.Checked:
            self.setWindowTitle('QCheckBox')
        else:
            self.setWindowTitle('')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())