import sys
from PyQt5.QtWidgets import *

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Pyqt Project")
        self.setGeometry(30,30,500,500)
        self.unitUI()
        self.show()

    def unitUI(self):
        self.tabs = QTabWidget(self) #sekme zemini
        self.tabs.resize(500,500)
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tabs.addTab(self.tab1,"tab 1")
        self.tabs.addTab(self.tab2,"tab 2")
        self.tabs.addTab(self.tab3,"tab 3")
        vbox = QVBoxLayout()
        self.text = QLabel("hello pyqt")
        self.button = QPushButton("button")
        self.button.clicked.connect(self.button_fonk)
        vbox.addWidget(self.text)
        vbox.addWidget(self.button)
        self.tab1.setLayout(vbox)
        vbox.addStretch()

    def button_fonk(self):
        self.text.setText("button clicked")

app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())
