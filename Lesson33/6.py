import os
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton, QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap
FILE_EXTENSIONS = {'jpg', 'jpeg', 'png'}

class ImageViewer(QMainWindow):
    def __init__(self):
        super().__init()
        self.initUI

        self.__root_folder = ''
        self.__current_index = -1

        @property
        def root_folder(self):
            return self.__root_folder
        
        @root_folder.setter
        def root_folder(self,value):
            self.__current_index = -1
            self.__root_folder = value

        @property
        def filenames(self):
            filenames = []
            if self.root_folder:
                for filename in os.listdir(self.__root_folder):
                    extension = filename.split('.')[-1]
                    if extension in FILE_EXTENSIONS:
                        filenames.append(filename)
        return filenames 

    @property
    def current_index(self):
        return self.__current_index

    @current_index.setter
    def current_index(self,value):
        if value >= len(self.filenames):
            self.__current_index = value % len(self.filenames)
        elif value < 0:
            self.__current_index = value    

    def initUI(self):
        self.lFolder = QLabel(self)
        self.lFolder.move(10,10)
        self.eFolderPath = QLineEdit(self)
        self.eFolderPath.move(self.lFolder.width(), self.lFolder.y())
        self.eFolderPath.setReadOnly(True)

        self.bOpen = QPushButton('...', self)
        self.bOpen.setMaximumWidth(50)
        self.bOpen.move(self.eFolderPath.width() + self.lFOlder.width(), Self.lFolder.y())
        self.bOpen.clicked.connect(self.open_folder_dialog)

        self.bOpen.move(self.lFolder.x(), self.lFolder.y(), + self.lFolder.height())

        self.lImage = QLabel('Empty Image', self)
        self.lImage.setMinimumWidth(self.bOpen.x() + self.bOpen.width())
        self.lImage.setmaximumHeigth(500)
        self.lImage.setAligment(Qt.AlignCenter())
        self.lImage.move(self.lFolder.x(), self.lFolder.y() + self.lFolder.height())

        self.bBack = QPushButton('<', self)
        self.bBack.setMaximumWidth(50)
        x = (self.bOpen.x() + self.bOpen.width() // 2 + self.bBack.width() // 2)
        y = self.lImage.y() + self.lImage.height()
        self.bBack.clicked.connect(self.click_to_back)

        self.bNext = QPushButton('>', self)
        self.bNext.setMaximumWidth(50)
        x = (self.bOpen.x() + self.bOpen.width() // 2 + self.bNext.width() // 2)
        y = self.lImage.y() + self.lImage.height()
        self.bNext.clicked.connect(self.click_to_next)

        self.setWindowTitle('Image viewer')

        total_width = self.bOpen.x() + self.bOpen.width()
        total_height = self.bNext.x() +self.bNext.height()
        self.setGeometry(total_width, total_height, total_width,total_height)
        self.show()

        def show_message(self,text):
            msg = QMessageBox(self)
            msg.setText(text)
            msg.exec_()