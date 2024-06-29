import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Pyqt Project")
        self.setGeometry(30,30,500,500)
        self.unitUI()
        self.show()
        self.fileOpen()

    def fileOpen(self):
        url = QFileDialog.getOpenFileName(self,"select file","","All Files(*);;*txt *py") #2.si özel bir yol tanımlamak için 3.sü berirli soya türlerinin gözükmesi için
        print(url)
        file = open(url[0],'r')
        content = file.read()
        self.label.setText(content)
        print(type(url[0]))
        print("type of url")

    def unitUI(self):
        self.label = QLabel("hello pyqt",self)

app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())
