import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLCDNumber, QSlider
from PyQt5.QtWidgets import QVBoxLayout, QApplication

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    # def init_ui(self):
    #     lcd = QLCDNumber(self)
    #     sld = QSlider(Qt.Horizontal, self)
    #     vbox = QVBoxLayout()
    #     vbox.addWidget(lcd)
    #     vbox.addWidget(sld)
    #     self.setLayout(vbox)
    #     sld.valueChanged.connect(lcd.display)
    #     self.setGeometry(300, 300, 250, 150)
    #     self.setWindowTitle('Signal & slot')
    #     self.show()

    def init_ui(self):
        self.setGeometry(300,300,250,150)
        self.setWindowTitle('Signal & slot')
        self.show()

    def KeyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
