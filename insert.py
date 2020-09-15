from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtPrintSupport import *
import sys
#import sqlite3
import time
import os


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

        # Janela do inserir.
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

        # Caixa de texto do nome.
        self.nameInput = QLineEdit()
        self.nameInput.setPlaceholderText("Nome")
        layout.addWidget(self.nameInput)

        # Combo Box.
        self.courseInput = QComboBox()
        self.courseInput.addItem("Português")
        self.courseInput.addItem("Inglês")
        self.courseInput.addItem("Matemática")
        self.courseInput.addItem("Física")
        self.courseInput.addItem("Química")
        self.courseInput.addItem("Ed. Física")
        self.courseInput.addItem("Biologia")
        self.courseInput.addItem("História")
        self.courseInput.addItem("Geografia")
        layout.addWidget(self.courseInput)

        # Selecionar no combo box.
        self.semInput = QComboBox()
        self.semInput.addItem("1")
        self.semInput.addItem("2")
        self.semInput.addItem("3")
        self.semInput.addItem("4")
        self.semInput.addItem("5")
        self.semInput.addItem("6")
        self.semInput.addItem("7")
        self.semInput.addItem("8")
        self.semInput.addItem("9")
        layout.addWidget(self.semInput)

        # Layout do local de texto para telefone.
        self.telInput = QLineEdit()
        self.telInput.setPlaceholderText("Nº Telefone")
        layout.addWidget(self.telInput)

        # Layout do local de texto para endereço.
        self.addressInput = QLineEdit()
        self.addressInput.setPlaceholderText("Endereço")
        layout.addWidget(self.addressInput)

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