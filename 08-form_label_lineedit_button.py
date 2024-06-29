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
        form = QFormLayout()
        hbox2 = QHBoxLayout()
        form.setRowWrapPolicy(QFormLayout.WrapAllRows) 
        #labelları form girişlerin üstüne almak için
        name_text = QLabel("your name: ")
        name_input = QLineEdit()
        password_text = QLabel("your password: ")
        password_input = QLineEdit()
        form.addRow(name_text,hbox2) #sadece ismin input ve labelını alabilir
        form.addRow(password_text,password_input) 
        form.addRow(QLabel("city"),QComboBox())
        hbox2.addWidget(name_input)
        hbox2.addWidget(QLineEdit())
        hbox = QHBoxLayout()
        hbox.addWidget(QPushButton("entry"))
        hbox.addWidget(QPushButton("exit"))
        form.addRow(hbox)
        self.setLayout(form)

app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())
