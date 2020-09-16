"""""
    Aqui será criada a tela de login.
    A verificação será feita no main.py, caso o login == False, ele abre a jánela de login.
"""
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtPrintSupport import *
import sys
import time
import os


"""
    Classe responsável por criar a janela de login.

    - def: __init__
        :param: self
        :param: *args
        :param: **kargs
    - def: check_password
        :param: self
"""
class LoginForm(QDialog):
    def __init__(self, *args, **kargs):
        super(LoginForm, self).__init__(*args, **kargs)
        self.setWindowIcon(QIcon("icon/login_icon.png"))

        # Botão deletar.
        self.QBtn = QPushButton()
        self.QBtn.setText("Login")

        # Janela de login
        self.setWindowTitle("Login")
        self.setFixedWidth(300)
        self.setFixedHeight(200)

        # Conexão.
        self.QBtn.clicked.connect(self.check_password)

        # Cria o grid do login.
        layout = QVBoxLayout()

        # Local onde se coloca o usuário.
        label_name = QLabel('<font size="4"> Username </font>')
        self.lineEdit_username = QLineEdit()
        self.lineEdit_username.setPlaceholderText("Digite seu nome de usuário")
        layout.addWidget(label_name)
        layout.addWidget(self.lineEdit_username)

        # Layout para password.
        label_password = QLabel('<font size="4"> Password </font>')
        self.lineEdit_password = QLineEdit()
        self.lineEdit_password.setPlaceholderText("Digite sua palavra-passe")
        layout.addWidget(label_password)
        layout.addWidget(self.lineEdit_password)

        layout.addWidget(self.QBtn)
        self.setLayout(layout)

    # Checagem de password, a ser corrigida para verificar os passwords e usernames no DB.
    def check_password(self):
        msg = QMessageBox()

        if self.lineEdit_username.text() == "Username" and self.lineEdit_password.text() == "000":
            msg.setWindowIcon(QIcon("icon/done.png"))
            msg.setWindowTitle("Efetuado")
            msg.setText("Sucesso")
            msg.exec_()
            app.quit()
        else:
            msg.setWindowIcon(QIcon("icon/failure.png"))
            msg.setWindowTitle("Não efetuado")
            msg.setText("Palavra-passe incorreta")
            msg.exec_()
