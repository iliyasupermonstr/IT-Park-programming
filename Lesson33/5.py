import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout
from PyQt5.QtGui import QPixmap

PATH = r'/Users/iliyabezrukov/projects/It-Park Course/Lesson33/IMG_3611.PNG'

class SimpleApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        hbox = QHBoxLayout(self)
        pixmap = QPixmap(PATH)

        lbl = QLabel(self)
        lbl.setPixmap(pixmap)
        hbox.addWidget(lbl)
        self.setLayout(hbox)
        self.move(300,300)
        self.setWindowTitle('DANKA STYLE')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SimpleApp()
    sys.exit(app.exec_())