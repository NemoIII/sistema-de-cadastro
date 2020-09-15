"""
    Aqui será criada a tela de login.
    A verificação será feita no main.py, caso o login == False, ele abre a jánela de login.
"""
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout, QMessageBox)

"""
    Classe responsável por criar a janela de login.

    - def: __init__
        :param: self
        :param: *args
        :param: **kargs
    - def: check_password
        :param: self
"""
class LoginForm(QWidget):
    def __init__(self, *args, **kargs):
        super(LoginForm, self).__init__(*args, **kargs)
        self.setWindowIcon(QIcon("icon/login_icon.png.png"))
        self.setWindowTitle("Login")
        self.resize(500, 300)

        # Cria o grid do login.
        layout = QGridLayout()

        # Local onde se coloca o usuário.
        labal_name = Qlabel('<font size="4"> Username </font>')
        self.lineEdit_username = QLineEdit()
        self.lineEdit_username.setPlaceholderText("Por favor, digite seu nome de usuário")
        layout.addWidget(labal_name, 0, 0)
        layout.addWidget(self.lineEdit_username, 0, 1)

        # Layout para password.
        label_password = QLabel("<font size='4'> Username </font>")
        self.lineEdit_password = QLineEdit()
        self.lineEdit_password.setPlaceholderText("Por favor, digite sua palavra-passe")
        layout.addWidget(label_password, 1, 0)
        layout.addWidget(self.lineEdit_password, 1, 1)

        # Botão de login.
        button_login = QPushButton("Login")
        button_login.clicked(self.check_password)
        layout.addWidget(button_login, 2, 0, 1, 2)
        layout.setRowMinimumHeight(2, 75)

        self.setLayout(layout)

    # Checagem de password, a ser corrigida para verificar os passwords e usernames no DB.
    def check_password(self):
        msg = QMessageBox()

        if self.lineEdit_username.text() == "Username" and self.lineEdit_password.text() == "000":
            msg.setText("Sucesso")
            msg.exec_()
            app.quit()
        else:
            msg.setText("Palavra-passe incorreta")
            msg.exec_()

"""if __name__ == '__main__':
	app = QApplication(sys.argv)

	form = LoginForm()
	form.show()

	sys.exit(app.exec_())"""