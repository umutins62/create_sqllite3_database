import os
import sqlite3
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout


class create_database(QWidget):
    def __init__(self):
        super().__init__()
        self.setUI()


    def setUI(self):
        self.setWindowTitle("Create Database")
        self.setGeometry(800,200,400,100)
        #create widgets
        self.databasename=QLineEdit()
        self.databasename.setPlaceholderText("Enter Database Name")
        self.tablename=QLineEdit()
        self.tablename.setPlaceholderText("Enter Table Name")
        self.createbutton=QPushButton("Create")
        self.createbutton.clicked.connect(self.create_database_)

        vbox=QVBoxLayout()
        vbox.addWidget(self.databasename)
        vbox.addWidget(self.tablename)
        vbox.addStretch()
        vbox.addWidget(self.createbutton)

        self.setLayout(vbox)
        self.show()

    def create_database_(self):

            try:
                if self.databasename.text()!="" or self.tablename.text()!="":
                    dbname=self.databasename.text()
                    tablename=self.tablename.text()
                    if os.path.exists(dbname+".db"):
                        self.setWindowTitle("Database exists")
                    else:
                        conn_obj=sqlite3.connect(dbname+".db")
                        cr_obj=conn_obj.cursor()
                        cr_obj.execute("DROP TABLE IF EXISTS "+tablename)
                        table=f""" CREATE TABLE {tablename} (
                                  id INTEGER PRIMARY KEY,
                                  name VARCHAR(50),
                                  age INTEGER,
                                  adress VARCHAR(255)
                                  ); """
                        cr_obj.execute(table)
                        self.setWindowTitle("create database with table")
                else:
                    self.setWindowTitle("please do not leave blank!")
            except:
                pass


if __name__=="__main__":
    app=QApplication(sys.argv)
    pencere=create_database()
    sys.exit(app.exec())






