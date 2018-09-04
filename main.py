#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 教程
在这个例子中, 我们用PyQt5创建了一个简单的窗口。

作者: Dengjm
网站: https://github.com/duduwolf/lottery
最后一次编辑: January 2015
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget


if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(600, 480)
    w.move(300, 300)
    w.setWindowTitle('看看谁是最幸运的人^_^')
    w.show()
    
    sys.exit(app.exec_())