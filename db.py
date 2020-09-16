from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtPrintSupport import *
import sys
import sqlite3
import time
import os
from insert import InsertDialog

class ConnectionDB():
    def __init__(self, *args, **kargs):
        super(ConnectionDB, self).__init__(*args, **kargs)
        self.conn = sqlite3.connect("register.db")

        self.db_cursor = self.conn.cursor()
        self.db_cursor.execute("CREATE TABLE IF NOT EXIST students (row INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, course TEXT, semester INTEGER, telephone INTEGER, address TEXT)")

        self.db_cursor.close()

    def load_data(self):
        self.connection = sqlite3.connect("register.db")
        query = "SELECT FROM * students"
        result = self.connection.execute(query)
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        # self.connection.close()

    def select_one_student(self, number):
        try:
            result = self.db_cursor.execute("SELECT * FROM students WHERE row = " + str(number))
            row = result.fetchone()
            search_result = "Nº Inscrição: " + str(row[0]) + "\n" + "Nome: " + str(row[1]) + "\n" + "Filial: " + str(row[2]) + "\n" + "Semestre: " + str(row[3]) + "\n" + "Telefone" + str(row[4]) + "\n" + "Endereço" + str(row[5])
            QMessageBox.information(QMessageBox(), "Pesquisa realizada com sucesso", search_result)
            self.conn.commit()
            self.db_cursor.close()
            self.conn.close()
        except Exception as err:
            QMessageBox.warning(QMessageBox(), "Aluno não encontrado", "Contacte o administrador do sistema.")

            