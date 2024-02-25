import json 
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from ui import Ui_MainWindow

class Widget(QMainWindow):
    def   __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.read_hotes()
        self.ui.listWidget.addItems(self.notes)
        self.ui.listWidget.itemClicked.connect(self.show_note)
        self.ui.save_btn.clicked.connect(self.save_notes)
        self.ui.deletezam_btn.clicked.connect(self.delete_note)
        self.ui.create_btn.clicked.connect(self.create_hotes)


    def show_note( self):
        self.name = self.ui.listWidget.selectedItems()[0].text()
        self.ui.title.setText(self.name)
        self.ui.texp.setText(self.notes[self.name]["текст"])


    def save_notes(self):
        self.notes[self.ui.title.text()] = {
            "текст": self.ui.texp.toPlainText(),
            "теги" : []
        }
        with open("notes.json","w", encoding="utf-8") as file:
            json.dump(self.notes , file)
        
        self.ui.zamitka.clear()
        self.ui.zamitka.addItems(self.notes)



    def clear(self):
        self.ui.title.clear()
        self.ui.texp.clear()


    def create_hotes(self):
        self.clear()


    def read_hotes(self):
        try:
            with open("notes.json" , "r" , encoding="utf-8") as file:
                self.notes = json.load(file)
        except:
            self.notes = {
            "Перша замітка":{
                "текст":"Це текст першої замітки",
                "теги": []
            }
        }




        
    def delete_note(self):
        try:
            del self.notes[self.name]
            self.clear()
            self.ui.zamitka.clear()
            self.ui.zamitka.addItems(self.notes)
            self.save_notes()
        except:
            print("помилка видалення")










app = QApplication([])
ex = Widget()
ex.show()
app.exec_()
