#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
抽奖窗口界面

作者: Dengjm
网站: https://github.com/duduwolf/lottery
"""

import sys
from PyQt5.QtWidgets import QToolTip, QPushButton, QApplication, QDesktopWidget, QMainWindow
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication

class Lottery_Windows(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()
        
        self.show()

    def initUI(self):
        
        #初始化窗口
        self.resize(1024, 768)
        self.__center()
        self.setWindowTitle("^_^  看看谁是最幸运的人  ^_^")
        self.setWindowIcon(QIcon("icon.png"))
        self.statusBar().showMessage("兰州市秦安路小学六年级三班")
        QToolTip.setFont(QFont("微软雅黑;SansSerif", 12))

        #初始化按钮
        sbtn = QPushButton("开始抽奖", self)
        sbtn.setToolTip("点击按钮开始抽奖")
        sbtn.resize(sbtn.sizeHint())
        sbtn.move(50, 50)
        sbtn.clicked.connect(self.start_lottery)
        sbtn.resize(100, 100)

        qbtn = QPushButton('退出', self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(300, 50)

    def __center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def start_lottery(self):
        print("点击开始按钮。。。")




if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    lw = Lottery_Windows()
    
    sys.exit(app.exec_())