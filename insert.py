from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtPrintSupport import *
import sys
#import sqlite3
import time
import os
from about import AboutDialog


"""
    Classe responsável por criar a janela de sobre.

    - def: __init__
        :param: self
        :param: *args
        :param: **kargs
    - def: add_student
        :param: self
"""
class InsertDialog(QDialog):
    def __init__(self, *args, **kargs):
        super(InsertDialog, self).__init__(*args, **kargs)
        self.setWindowIcon(QIcon("icon/note.png"))
        
        # Botão registrar.
        self.QBtn = QPushButton()
        self.QBtn.setText("Registrar")

        # Janela do sobre.
        self.setWindowTitle("Adicionar aluno:")
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        # Formulário.
        self.setWindowTitle("Dados do aluno:")
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        # Conexão.
        self.QBtn.clicked.connect(self.add_student)

        # Cria o layout.
        layout = QVBoxLayout()
        self.nameImput = QLineEdit()
        self.nameImput.setPlaceholderText("Nome")
        layout.addWidget(self.nameImput)

        # Combo Box.
        self.courseImput = QComboBox()
        self.courseImput.addItem("Português")
        self.courseImput.addItem("Inglês")
        self.courseImput.addItem("Matemática")
        self.courseImput.addItem("Física")
        self.courseImput.addItem("Química")
        self.courseImput.addItem("Ed. Física")
        self.courseImput.addItem("Biologia")
        self.courseImput.addItem("História")
        self.courseImput.addItem("Geografia")
        layout.addWidget(self.courseImput)

        # Selecionar no combo box.
        self.semImput = QComboBox()
        self.semImput.addItem("1")
        self.semImput.addItem("2")
        self.semImput.addItem("3")
        self.semImput.addItem("4")
        self.semImput.addItem("5")
        self.semImput.addItem("6")
        self.semImput.addItem("7")
        self.semImput.addItem("8")
        self.semImput.addItem("9")
        layout.addWidget(self.semImput)

        # Layout do local de texto para telefone.
        self.telImput = QLineEdit()
        self.telImput.setPlaceholderText("Nº Telefone")
        layout.addWidget(self.telImput)

        # Layout do local de texto para endereço.
        self.addressImput = QLineEdit()
        self.addressImput.setPlaceholderText("Endereço")
        layout.addWidget(self.addressImput)

        layout.addWidget(self.QBtn)
        self.setLayout(layout)

    def add_student(self):
        name = ""
        course = ""
        sem = -1
        tel = ""
        address = ""

        name = self.nameImput.text()
        course = self.courseImput.itemText(self.courseImput.currentIndex())
        sem = self.semImput.itemText(self.semImput.currentIndex())
        tel = self.telImput.text()
        address = self.addressImput.text()