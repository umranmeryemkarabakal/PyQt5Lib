import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont # font için
from PyQt5.QtGui import QPixmap # fotoğraf,resimler için

FONT = QFont("Times New Roman",14) # font adı, punto

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("pyqt example") # pencerenin başlığı
        self.setGeometry(40, 40, 800, 1000) 
        # (40,40) koordinatlarından başlar 400'e 400 dikdörtgen oluşturur
        self.initUI() # fonksiyonu çağıralım
        self.show() # pencereyi göster

    def initUI(self):
        self.label1 = QLabel("hello pyqt", self) 
        # label hem resim hem yazı eklemek için kullanılır
        # başına konulan self ile bunun başka fonsiyon tarafından kullanılmasını sağlar, parantez için içine konulan self kendi ekranınmda objemde göster, ekle demektir
        self.label1.setFont(FONT) #f ontunu ayarlar
        self.label1.move(100,40) # (100,40) koordinatına taşır
        
        self.button1 = QPushButton("button click",self) 
        # buttonun üzerindeki yazı,self parametresi
        self.button1.move(100,80) # (100,80) koordinatlarına taşı
        self.button1.setFont(FONT)
        self.button1.clicked.connect(self.funcbutton1) 
        # buton ile fonksiyon arasındaki bağlantı

        self.button2 = QPushButton("button click",self)
        self.button2.move(300,80)
        self.button2.setFont(FONT)
        self.button2.clicked.connect(lambda: self.funcbutton2("button 2 pressed"))

        self.label2 = QLabel(self)
        self.label2.setFont(FONT)

        self.namebox = QLineEdit(self) # entry giriş kutusu
        self.namebox.move(100,230)
        self.namebox.setPlaceholderText("entry your name") 
        # entry'nin içinde hind olarak yazılan yazı

        self.passwordbox = QLineEdit(self)
        self.passwordbox.move(100,280)
        self.passwordbox.setPlaceholderText("entry your password")
        self.passwordbox.setEchoMode(QLineEdit.Password) 
        # password paramteresi ile şifre gizlenir

        self.man = QCheckBox("man",self) # işaretleme kutusu
        self.man.move(100, 320)

        self.woman = QCheckBox("woman", self)
        self.woman.move(180, 320)

        self.button3 = QPushButton("save", self)
        self.button3.move(100, 370)
        self.button3.clicked.connect(self.save)
 
        self.picture = QLabel(self) 
        # fotoğraf eklemek içinde label kullanılır
        original_pixmap = QPixmap("img.png") 
        # "img.png" adlı dosyadan bir QPixmap nesnesi oluşturulur
        scaled_pixmap = original_pixmap.scaled(300, 150)   
        # Orijinal QPixmap nesnesi, 300x150 boyutlarına küçültülür.
        self.picture.setPixmap(scaled_pixmap)  
        # QLabel'e küçültülmüş QPixmap nesnesi atanır.
        self.picture.setFixedSize(300, 150) 
        # QLabel'in boyutu 300x150 piksel olarak ayarlanıyor.
        self.picture.move(100,430)

        self.combobox = QComboBox(self)
        self.combobox.move(100,600)
        self.combobox.addItem("python")
        self.combobox.addItems(["java","javascript","C","C++","C#"]) # sadece string alır
        my_list = ["objective-c","ruby","assembly","go","php"]
        for programming_launage in my_list:
            self.combobox.addItem(programming_launage)
        self.combobox.activated.connect(self.select)

        self.textEdit = QTextEdit(self)
        self.textEdit.move(100, 640)
        self.textEdit.setAcceptRichText(False)  
        # zengin metin özelliğini ayarla kopy-paste yaparken yazıyı özellikleriyle almaması için kullanılır

        self.button4 = QPushButton("selected",self)
        self.button4.move(100,840)
        self.button4.clicked.connect(self.selectwithbutton)

    def selectwithbutton(self):
        text = self.combobox.currentText()
        print(text)

        textEdit = self.textEdit.toPlainText()
        print(textEdit)
    def select(self):
        text = self.combobox.currentText() #current txt : geçerli text
        print(text)
    def save(self):
        messagebox = QMessageBox.question(self,"warning","Are you sure you want to save?",QMessageBox.Yes | QMessageBox.No) #mesaj kutusu oluşturma
        if messagebox == QMessageBox.No: # eğer no işaretlendiyse
            sys.exit() # programın tamamından çıkar,window deseydik sadece ekran kapanırdı

        name = self.namebox.text() # name entrysinin içindeki texti alır
        password = self.passwordbox.text()

        self.label2.setText("welcome " + name) # label'ı set ile tekrar yazdırır
        self.label2.setGeometry(100,200,200,20)

        print(self.man.isChecked()) 
        # man'in işaretlenip işaretlenmediğini kontrol eeder, şaretlendiyse True döndürür

        if self.man.isChecked():
            print("gender: man")
        else:
            print("gender: women")
    def funcbutton1(self):
        # self.label1.resize(100,60) #labelı yeniden boyutlar
        self.label1.setText("button clicked") # labelda yazısını değiştirir
        self.setWindowTitle("button active") # window title'ı değiştirir
        self.button2.close() # buttton 2 yi kaldırır
    def funcbutton2(self,message):
        # self.label1.resize(100,60)
        self.label1.setText(message)
        self.setWindowTitle("button inactive")
        self.button1.close()

app = QApplication(sys.argv)
window = Window() #pencere oluşturur
sys.exit(app.exec_()) #execuetable : çalıştırılabilir
#app nesnesi, genellikle bir uygulama penceresini temsil eden bir objedir.
#exec_() fonksiyonu, GUI uygulamasının ana döngüsünü başlatır ve kullanıcının etkileşimde bulunmasını bekler.
#sys.exit() fonksiyonu ise, uygulama kapatıldığında programın düzgün bir şekilde sonlanmasını sağlar.