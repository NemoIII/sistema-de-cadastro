from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtPrintSupport import *
import sys
import time
import os
#from db import ConnectionDB


"""
    Classe responsável por criar a janela de pesquisa.

    - def: __init__
        :param: self
        :param: *args
        :param: **kargs
    - def: search_student
        :param: self
"""
class SearchDialog(QDialog):
    def __init__(self, *args, **kargs):
        super(SearchDialog, self).__init__(*args, **kargs)
        self.setWindowIcon(QIcon("icon/computer.png"))

        # Botão pesquisar.
        self.QBtn = QPushButton()
        self.QBtn.setText("Pesquisar")

        # Janela do pesquisar.
        self.setWindowTitle("Pesquisar aluno")
        self.setFixedWidth(300)
        self.setFixedHeight(100)

        # Botão de clique.
        self.QBtn.clicked.connect(self.search_student)

        # Cria o layout.
        layout = QVBoxLayout()

        # Layout do local de texto para pesquisar e validar o nº de inscrição.
        label_search = QLabel('<font size="4"> Nº Inscrição </font>')
        self.searchInput = QLineEdit()
        self.onlyInt = QIntValidator()
        self.searchInput.setValidator(self.onlyInt)
        self.searchInput.setPlaceholderText("Nº Inscrição")
        layout.addWidget(label_search)
        layout.addWidget(self.searchInput)

        # Botão validador
        layout.addWidget(self.QBtn)
        self.setLayout(layout)

    def search_student(self):
        #from db import ConnectionDB
        search_row = ""
        search_row = self.searchInput.text()
        #ConnectionDB().load_one_student(search_row)