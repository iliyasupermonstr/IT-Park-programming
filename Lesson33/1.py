import sys
from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication,QFrame,
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        cb = QCheckBox('Show title', self)
        cb.move(20,20)
        cb.toggle()
        cb.stateChanged.connect(self.change_title)
        self.setGeometry(300,300,250,150)
        self.setWindowTitle('QCheckBox')
        self.show()

    def change_title(self, state):
        if state == Qt.Checked:
            self.setWindowTitle('QCheckBox')
        else:
            self.setWindowTitle('')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())