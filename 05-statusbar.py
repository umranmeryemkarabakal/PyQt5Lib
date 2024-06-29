import sys
from PyQt5 import QtWidgets

class UnitUI(QtWidgets.QMainWindow):
    def __init__(self):
        super(UnitUI,self).__init__()
        self.setWindowTitle("progress bar example")
        self.setGeometry(300,200,500,500)
        self.progressbar = QtWidgets.QProgressBar(self)
        self.button = QtWidgets.QPushButton("start",self)
        self.show()
        self.gui_configuration()

    def gui_configuration(self):
        self.progressbar.resize(400,50)
        self.progressbar.move(50,200)
        self.button.move(150,300)
        self.button.clicked.connect(self.take_action)

    def take_action(self):
        self.number = 0

        while(self.number <= 100):
            self.progressbar.setValue(self.number)
            self.number += 0.0001

if __name__ == "main":
    app = QtWidgets.QApplication(sys.argv)
    Window = UnitUI()
    sys.exit(app.exec_())