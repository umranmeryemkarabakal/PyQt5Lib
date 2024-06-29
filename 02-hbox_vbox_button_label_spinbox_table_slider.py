import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt #slider için

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Pyqt Project")
        self.setGeometry(30, 30, 500, 500)
        self.unitUI()
        self.show()

    def unitUI(self):
        
        horizontalbox = QHBoxLayout() #QV:vertical box layout QH: horizontal box layout
        button1 = QPushButton("button 1")
        button2 = QPushButton("button 2")
        button3 = QPushButton("button 3")
        horizontalbox.addWidget(button1)
        horizontalbox.addWidget(button2)
        horizontalbox.addWidget(button3)
        self.setLayout(horizontalbox) #horizontal box pencereye eklenir
        
        # yukarı ve aşağı stretch (itikleme gibi) vertical box için, sağ sola stretch horizantol box için kullanılır

        horizontalbox1 = QHBoxLayout() #QV:vertical box layout QH: horizontal box layout
        button4 = QPushButton("button 4")
        button5 = QPushButton("button 5")
        button6 = QPushButton("button 6")
        horizontalbox1.addStretch()
        horizontalbox1.addWidget(button4)
        horizontalbox1.addWidget(button5)
        horizontalbox1.addWidget(button6)
        horizontalbox1.addStretch()
        self.setLayout(horizontalbox1)
        
        # dizayn elemanlarını yan yana dizmek için horizontal layout kullanılır, alt alta dizmek için vertical box kullanılır

        verticalbox = QVBoxLayout()
        button7 = QPushButton("button 7")
        button8 = QPushButton("button 8")
        button9 = QPushButton("button 9")
        verticalbox.addStretch()
        verticalbox.addWidget(button7)
        verticalbox.addWidget(button8)
        verticalbox.addWidget(button9)
        verticalbox.addStretch()
        self.setLayout(verticalbox)
                
        self.spinbox = QSpinBox(self)
        self.spinbox.move(130,100)
        #self.spinbox.setMaximum(25)
        #self.spinbox.setMinimum(10)
        self.spinbox.setRange(10,25)
        self.spinbox.setSingleStep(2) #2şerli ilerler
        #dolar birimi önde lira,cm,m birimi sonda
        self.spinbox.setPrefix("$ ") # ön birim
        self.spinbox.setSuffix(" cm") # arka birim
        self.spinbox.valueChanged.connect(self.get_value)
        
        self.table = QTableWidget(self)
        self.table.setRowCount(5)
        self.table.setColumnCount(3)
        self.table.resize(350,350)
        myList = ["name","surname","age"]
        self.table.setHorizontalHeaderItem(0,QTableWidgetItem(myList[0]))
        self.table.setHorizontalHeaderItem(1,QTableWidgetItem(myList[1]))
        self.table.setHorizontalHeaderItem(2,QTableWidgetItem(myList[2]))
        #self.table.horizontalHeader().hide() #sütun isimleri gizle
        #self.table.verticalHeader().hide() #satır isimlerini gizle
        self.table.setItem(0,0,QTableWidgetItem("meryem"))
        self.table.setItem(0,1,QTableWidgetItem("karabakal"))
        self.table.setItem(0,2,QTableWidgetItem("18"))
        #şu anda toblo içi kullanıcı tarafından değiştirilebilir
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers) 
        #kullanıcı içindeki veriyi değiştiremez
        self.table.doubleClicked.connect(self.get_item)
        #kullanıcı hangi veriye click yaptı
        
        verticalbox2 = QVBoxLayout()
        self.text1 = QLabel("0")
        self.text2 = QLabel("hello pyqt")
        self.text1.setAlignment(Qt.AlignCenter)
        self.slider1 = QSlider(Qt.Horizontal)
        self.slider1.setMinimum(0)
        self.slider1.setMaximum(70)
        self.slider1.setTickPosition(QSlider.TicksAbove)
        self.slider1.setTickInterval(5) #tick aralığı 5er 5er
        self.slider1.valueChanged.connect(self.get_value_slider)
        verticalbox2.addStretch()
        verticalbox2.addWidget(self.slider1)
        verticalbox2.addWidget(self.text1)
        verticalbox2.addWidget(self.text2)
        self.setLayout(verticalbox2)
        
    def get_value_slider(self):
        self.text1.setText(str(self.slider1.value()))
        font_size = self.slider1.value()
        FONT = QFont("arial",font_size)
        self.text2.setFont(FONT)

    def get_item(self):
      for item in self.table.selectedItems():
            print(item.text(), item.row(), item.column())

    def get_value(self):
        print(self.spinbox.value())

def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
    