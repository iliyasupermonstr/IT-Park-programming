import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Создание кнопки Button 1
        btn1 = QPushButton("Button 1", self)
        btn1.move(30, 50)

        # Создание кнопки Button 2
        btn2 = QPushButton("Button 2", self)
        btn2.move(150, 50)

        # Подключение сигналов от кнопок к методу click_button
        btn1.clicked.connect(self.click_button)
        btn2.clicked.connect(self.click_button)

        # Создание статусной строки
        self.statusBar()
        
        # Установка размеров и заголовка окна
        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Button Example')
        
        # Показ окна
        self.show()

    def click_button(self):
        # Получение объекта отправителя
        sender = self.sender()
        # Показ сообщения в статусной строке
        self.statusBar().showMessage(sender.text() + ' was pressed')

# Запуск приложения
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
