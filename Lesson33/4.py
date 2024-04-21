import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QCalendarWidget
from PyQt5.QtCore import QDate

class SimpleApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        cal = QCalendarWidget(self)
        cal.setGridVisible(True)
        cal.move(20,20)
        cal.clicked[QDate].connect(self.show_date)
        
        self.lbl = QLabel(self)
        date = cal.selectedDate()
        self.lbl.setText(date.toString())
        self.lbl.move(130,260)
        self.show()
    
    def show_date(self,date):
        self.lbl.setText(date.toString())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SimpleApp()
    sys.exit(app.exec_())