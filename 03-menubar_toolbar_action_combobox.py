import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("pyqt Project")
        self.setGeometry(30,30,500,500)
        self.unitUI()
        self.show()

    def unitUI(self):
        # ana menu
        menubar = self.menuBar()
        file = menubar.addMenu("file")
        edit = menubar.addMenu("edit")
        code = menubar.addMenu("code")
        helpme = menubar.addMenu("help")

        # alt menu
        new = QAction("new project",self)
        new.setShortcut("Ctrl+o") # kısa yol atandı
        file.addAction(new)
        openn = QAction("open", self)
        file.addAction(openn)
        exitt = QAction("exit", self)
        exitt.setIcon(QIcon("img.png"))
        exitt.triggered.connect(self.exitt)
        file.addAction(exitt)

        # tool bar
        tool_bar = self.addToolBar("my tool bar")
        tool_bar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)  
        # iconun altında ismini yazılmasını sağlar
        new1 = QAction(QIcon("img.png"),"new",self)
        tool_bar.addAction(new1)
        openn2 = QAction(QIcon("img.png"), "open", self)
        tool_bar.addAction(openn2)
        exitt1 = QAction(QIcon("img.png"),"exit",self)
        exitt1.triggered.connect(self.exitt) # triggered:tetiklenmiş
        tool_bar.addAction(exitt1)
        tool_bar.actionTriggered.connect(self.button_fonk) 
        # bir kaç butona aynı fonksyionu bağlamak için kullnılabilir
        self.combo_box = QComboBox()
        l = ["python","c++","javascript","ruby"]
        self.combo_box.addItems([l[0],l[1],l[2],l[3]])
        tool_bar.addWidget(self.combo_box)

    def button_fonk(self,button):
        if button.text() == "new":
            print("button 1 clicked")
        elif button.text() == "open":
            print("button 2 clicked")
        else:
            print("button pressed")

    def exitt(self):
        msgbox = QMessageBox.information(self,"warning","Are you sure you want to save?",QMessageBox.Yes | QMessageBox.No,QMessageBox.No )
        if msgbox== QMessageBox.Yes:
            sys.exit()

app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())
