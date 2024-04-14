import sys
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon, QFont

ICON = r'/Users/iliyabezrukov/projects/It-Park Course/Lesson31/2024-03-25 20.11.53.jpg'

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b>widget')
        self.setGeometry(300,300,300,220)
        self.setWindowTitle('Icon Test')
        self.setWindowIcon(QIcon(ICON))

        button = QPushButton('Quit', self)
        button.resize(button.sizeHint())

        button.move(100,100)
        button.clicked.connect(self.show_message)
        self.show()

    def show_message(self):
        message_box =QMessageBox()
        message_box.setIcon(QMessageBox.Information)
        message_box.setText('some text')
        message_box.exec_()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
    self.show()