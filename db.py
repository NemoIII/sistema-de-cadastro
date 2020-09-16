from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtPrintSupport import *
import sys
import sqlite3
import time
import os

class ConnectionDB():
    def __init__(self, *args, **kargs):
        super(ConnectionDB, self).__init__(*args, **kargs)
        self.conn = sqlite3.connect("register.db")

        self.db_cursor = self.conn.cursor()
        self.db_cursor.execute("CREATE TABLE IF NOT EXIST students (row INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, course TEXT, semester INTEGER, telephone INTEGER, address TEXT)")