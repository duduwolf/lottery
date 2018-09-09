#coding: utf-8

import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("client")
        self.setWindowIcon(QIcon('icons/icon.png'))
        self.resize(900, 700)
        self.show()

        self.browser = QWebEngineView()
        url = 'file:///Users/denglq/develop/python/lottery/index.html'
        self.browser.load(QUrl(url))
        self.setCentralWidget(self.browser)

if __name__=='__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())