import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Pyqt Project")
        self.setGeometry(30,30,500,500)
        self.unitUI()
        self.show()

    def unitUI(self):
        self.grid = QGridLayout()
        button1 = QPushButton("button 1")
        button1.clicked.connect(self.button_clicked)
        button2 = QPushButton("button 2")
        button3 = QPushButton("button 3")
        button4 = QPushButton("button 4")

        #self.grid.addWidget(button1,0,0)

        for i in range(0,3):
            for j in range(0,3):
                button = QPushButton("{}{}button".format(i,j))
                self.grid.addWidget(button,i,j)
                button.clicked.connect(self.button_clicked)
        self.setLayout(self.grid)

    def button_clicked(self):
        print("button clicked")
        button_id = self.sender().text()
        if button_id == "00button":
            print("button 1 clicked")

app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())