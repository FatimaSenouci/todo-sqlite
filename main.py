import os
import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
import sqlite3
# Create a database or connect to one
conn = sqlite3.connect("mytodoliste.db")
# Create cursor
c = conn.cursor()
# Create a table on database
c.execute(""" CREATE TABLE if not exists todolist(
      list_item text)
      """)
#commit the changes
conn.commit()
#close our connection
conn.close()

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        ui_path = os.path.dirname(os.path.abspath(__file__))
        uic.loadUi(os.path.join(ui_path, "untitled.ui"), self)
        self.show()
        self.Handel_Button()
        #self.Handel2()

        #self.AddpushButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.add())

    def Handel_Button(self):
        self.AddpushButton_2.clicked.connect(self.add)
        self.DeletepushButton_3.clicked.connect(self.delete)
        self.ClearpushButton_4.clicked.connect(self.clear)
        self.SavepushButton_5.clicked.connect(self.saveToDB)
    #def Handel2(self):
        #self.DeletepushButton_3.clicked.connect(self.delete)
        #Grab all the  items from database
        self.grab_all()
        #Grab  items from the database
    def grab_all(self):
         # Create a database or connect to one
         conn = sqlite3.connect("mytodoliste.db")
         # Create cursor
         c = conn.cursor()
         c.execute("SELECT * FROM todolist")
         records = c.fetchall()
         # commit the changes
         conn.commit()
         # close our connection
         conn.close()

         # loop thru records and add to sceen
         for record in records :
             self.MylistWidget_2.addItem(str(record[0]))



    def add(self):
        item = self.MylineEdit_2.text()
        self.MylistWidget_2.addItem(item)
        #clear line edite
        self.MylineEdit_2.clear()

    def delete(self):
        #Grab the selected row
        clickedItem = self.MylistWidget_2.currentRow()
        #get the index
         #self.MylineEdit.setText(str(clickedItem))
        #delete selected row
        self.MylistWidget_2.takeItem(clickedItem)
    def clear(self):
        self.MylistWidget_2.clear()


    #Save to data base
    def saveToDB(self):
        # Create a database or connect to one
        conn = sqlite3.connect("mytodoliste.db")
        # Create cursor
        c = conn.cursor()
        #delete everything in the database
        c.execute('DELETE FROM todolist ;',)

        # create blanck list to hold
        items = []
        #loop through the listewidget and pull out each item
        for index in range(self.MylistWidget_2.count()):
            items.append(self.MylistWidget_2.item(index))

        for item in items :
            #print(item.text())
            #add stuf to the table
            c.execute("INSERT INTO todolist VALUES (:item)",
      {
                          'item':item.text(),
                    })


        #commit the changes
        conn.commit()
        #close our connection
        conn.close()
        # pop up msg box
        msg = QMessageBox()
        msg.setWindowTitle(" Saved to database ")
        msg.setText("Your Todo Liste Has been Saved !")
        msg.setIcon(QMessageBox.Information)
        x = msg.exec_()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec_() #infinit loop to nit desqpeqred the app


if __name__ == "__main__":
    main()