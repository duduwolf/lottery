#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
抽奖窗口界面

作者: Dengjm
网站: https://github.com/duduwolf/lottery
"""

import sys
#from PyQt5.QtWidgets import QToolTip, QPushButton, QApplication, QDesktopWidget, QMainWindow
#from PyQt5.QtGui import QIcon, QFont
#from PyQt5.QtCore import QCoreApplication
from PyQt5 import QtWidgets, QtGui, QtCore

class Lottery_Windows(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        #self.initUI()
        self.initUI2(self)
        self.show()

    def initUI(self):
        
        #初始化窗口
        self.resize(1024, 768)
        self.__center()
        self.setWindowTitle("^_^  看看谁是最幸运的人  ^_^")
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.statusBar().showMessage("兰州市秦安路小学六年级三班")
        QtWidgets.QToolTip.setFont(QtGui.QFont("微软雅黑;SansSerif", 12))

        #初始化按钮
        sbtn = QtWidgets.QPushButton("开始抽奖", self)
        sbtn.setToolTip("点击按钮开始抽奖")
        sbtn.resize(sbtn.sizeHint())
        sbtn.move(50, 50)
        sbtn.clicked.connect(self.start_lottery)
        sbtn.resize(120, 60)
        sbtn.setFont(QtGui.QFont("微软雅黑;SansSerif", 18))

        qbtn = QtWidgets.QPushButton('退出', self)
        qbtn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(300, 50)
        qbtn.resize(120, 60)
        qbtn.setFont(QtGui.QFont("微软雅黑;SansSerif", 18))

    def __center(self):
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def start_lottery(self):
        print("点击开始按钮。。。")

    def initUI2(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        self.resize(748, 541)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(10, 30, 10, 20)
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(20)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.gridLayout.addWidget(self.widget, 1, 4, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.pushButton.setFont(font)
        self.pushButton.setDefault(False)
        self.pushButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 3, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.gridLayout.addWidget(self.pushButton_2, 3, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 3, 1, 1)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit.setFocusPolicy(QtCore.Qt.NoFocus)
        self.gridLayout.addWidget(self.plainTextEdit, 1, 3, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout.addWidget(self.frame_2, 2, 1, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 3, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 3, 4, 1, 1)
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 1, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 3, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        #self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "点击抽选"))
        self.pushButton_2.setText(_translate("MainWindow", "退      出"))
        self.label.setText(_translate("MainWindow", "看看今天谁是最幸运的人"))
        self.label_2.setText(_translate("MainWindow", "被抽中的名单"))

        self.pushButton_2.clicked.connect(QtCore.QCoreApplication.instance().quit)
        self.pushButton.clicked.connect(self.start_lottery)



if __name__ == '__main__':
    
    app = QtWidgets.QApplication(sys.argv)
    lw = Lottery_Windows()
    
    sys.exit(app.exec_())