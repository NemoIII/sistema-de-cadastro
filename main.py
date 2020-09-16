from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtPrintSupport import *
import sys
import time
import os
from about import AboutDialog
from insert import InsertDialog
from login import LoginForm
from search import SearchDialog
from delete import DeleteDialog
#from db import ConnectionDB

"""
    Classe responsável por criar a janela principal.

    - def: __init__
        :param: self
        :param: *args
        :param: **kargs
    - def: about
        :param: self
"""
class MainWindow(QMainWindow):
    def __init__(self, *args, **kargs):
        super(MainWindow, self).__init__(*args, **kargs)
        self.setWindowIcon(QIcon("icon/book.png"))

        # Botões da barra de ferramentas.
        file_menu = self.menuBar().addMenu("&File")
        help_menu = self.menuBar().addMenu("&Help")
        self.setWindowTitle("Cadastro de alunos")
        # Tamanho default da janela.
        self.setMinimumSize(800,600)

        # Criação da tabela com as informações a serem cadastradas.
        self.tableWidget = QTableWidget()
        self.setCentralWidget(self.tableWidget)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        self.tableWidget.setHorizontalHeaderLabels(("Inscrição nº", "Nome", "Filial", "Semestre", "Telefone", "Endereço"))

        # Inclusão de botões.
        toolbar = QToolBar()
        toolbar.setMovable(False)
        self.addToolBar(toolbar)

        ###################
        #   Status bar.   #
        ###################

        status_bar = QStatusBar()
        self.setStatusBar(status_bar)

        #######################
        #   Botões de acões.  #
        #######################

        # Botão de login de usuário.
        btn_ac_loginUser = QAction(QIcon("icon/login.png"), "Login", self)
        btn_ac_loginUser.triggered.connect(self.login)
        btn_ac_loginUser.setStatusTip("Login")
        toolbar.addAction(btn_ac_loginUser)

        # Botão de adicionar usuário.
        btn_ac_addUser = QAction(QIcon("icon/add1.png"), "Add Aluno", self)
        btn_ac_addUser.triggered.connect(self.insert)
        btn_ac_addUser.setStatusTip("Add Aluno")
        toolbar.addAction(btn_ac_addUser)

        # Botão de atualizar usuário.
        btn_ac_refresh = QAction(QIcon("icon/refresh.png"), "Atualizar Aluno", self)
        btn_ac_refresh.setStatusTip("Atualizar Aluno")
        toolbar.addAction(btn_ac_refresh)

        # Botão de pesquisar usuário.
        btn_ac_search = QAction(QIcon("icon/search.png"), "Pesquisar Aluno", self)
        # ToDo: testar o sqlite3 na minha própria máquina, pois nessa aqui não está a funcionar.
        #btn_ac_search.triggered.connect(ConnectionDB.select_one_student(number))
        btn_ac_search.triggered.connect(self.search)
        btn_ac_search.setStatusTip("Pesquisar Aluno")
        toolbar.addAction(btn_ac_search)

        # Botão de deletar usuário.
        btn_ac_delete = QAction(QIcon("icon/delete.png"), "Deletar Aluno", self)
        btn_ac_delete.triggered.connect(self.delete)
        btn_ac_delete.setStatusTip("Deletar Aluno")
        toolbar.addAction(btn_ac_delete)

        #####################
        #   Barra de menu.  #
        #####################
        
        # Botão de login de usuário.
        login_user_action = QAction(QIcon("icon/login.png"), "Login", self)
        login_user_action.triggered.connect(self.login)
        file_menu.addAction(login_user_action)

        # Botão de adicionar usuário.
        add_user_action = QAction(QIcon("icon/add1.png"), "Add Aluno", self)
        add_user_action.triggered.connect(self.insert)
        file_menu.addAction(add_user_action)

        # Botão de atualizar usuário.
        refresh_user_action = QAction(QIcon("icon/refresh.png"), "Atualizar Aluno", self)
    #refresh_user_action.triggered.connect(self.refresh)
        file_menu.addAction(btn_ac_refresh)

        # Botão de pesquisar usuário.
        search_user_action = QAction(QIcon("icon/search.png"), "Pesquisar Aluno", self)
        search_user_action.triggered.connect(self.search)
        file_menu.addAction(search_user_action)

        # Botão de deletar usuário.
        delete_user_action = QAction(QIcon("icon/delete.png"), "Deletar Aluno", self)
        delete_user_action.triggered.connect(self.delete)
        file_menu.addAction(delete_user_action)

        # Botão de deletar usuário.
        about_action = QAction(QIcon("icon/data.png"), "Developer", self)
        about_action.triggered.connect(self.about)
        help_menu.addAction(about_action)

    def login(self):
        dlg = LoginForm()
        dlg.exec_()

    def insert(self):
        dlg = InsertDialog()
        dlg.exec_()
    
    def search(self):
        dlg = SearchDialog() #.search_student()
        dlg.exec_()

    def delete(self):
        dlg = DeleteDialog() #.delete_student()
        dlg.exec_()

    def about(self):
        dlg = AboutDialog()
        dlg.exec_()

    """def connection(self):
        dlg = ConnectionDB()
        dlg.exec_()"""


if __name__ == "__main__":
    app = QApplication(sys.argv)
    if (QDialog.Accepted == True):
        window = MainWindow()
        window.show()
        #window.ConnectionDB().load_data()
sys.exit(app.exec_())
