# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.Qt import *
from PyQt5 import QtCore, QtGui, QtWidgets
import subprocess


class Ui_RemoteConnect(object):
    def setupUi(self, RemoteConnect):
        RemoteConnect.setObjectName("RemoteConnect")
        RemoteConnect.resize(546, 331)
        palette = QPalette()
        #背景图片
        pix = QPixmap("./under1.png")
        pix = pix.scaled(RemoteConnect.width(), RemoteConnect.height())
        palette.setBrush(QPalette.Background, QBrush(pix))
        RemoteConnect.setPalette(palette)
        self.pushButton = QtWidgets.QPushButton(RemoteConnect)
        self.pushButton.setGeometry(QtCore.QRect(80, 270, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton.setIconSize(QtCore.QSize(16, 16))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(RemoteConnect)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 270, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit = QtWidgets.QLineEdit(RemoteConnect)
        self.lineEdit.setGeometry(QtCore.QRect(150, 90, 271, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setPlaceholderText("请输入连接IP")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(RemoteConnect)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 150, 271, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setPlaceholderText("请输入登陆账号")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(RemoteConnect)
        self.lineEdit_3.setGeometry(QtCore.QRect(150, 210, 271, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_3.setPlaceholderText("请输入连接密码")
        self.lineEdit_3.setEchoMode(QLineEdit.Password)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label = QtWidgets.QLabel(RemoteConnect)
        self.label.setGeometry(QtCore.QRect(60, 100, 70, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(RemoteConnect)
        self.label_2.setGeometry(QtCore.QRect(60, 160, 70, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(RemoteConnect)
        self.label_3.setGeometry(QtCore.QRect(60, 220, 70, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.retranslateUi(RemoteConnect)
        QtCore.QMetaObject.connectSlotsByName(RemoteConnect)

    def retranslateUi(self, RemoteConnect):
        _translate = QtCore.QCoreApplication.translate
        RemoteConnect.setWindowTitle(_translate("RemoteConnect", "Remote Connect"))
        self.pushButton.setText(_translate("RemoteConnect", "Connect"))
        self.pushButton_2.setText(_translate("RemoteConnect", "Cancel"))
        self.label.setText(_translate("RemoteConnect", "IP "))
        self.label_2.setText(_translate("RemoteConnect", "UserName"))
        self.label_3.setText(_translate("RemoteConnect", "Password"))
        # self.pushButton.clicked.connect(connectTo)
        # self.pushButton_2.clicked.connect(closeWindow)

    def connectTo(self, button):
        try:
            code = -1
            command = [
                "/usr/bin/xfreerdp",
                "-K",
                "-g", "workarea",
                "--ignore-certificate",
                "--rfx",
                "--rfx-mode", "video",
                "--plugin", "cliprdr",
                "--plugin", "rdpsnd", "--data", "alsa", "--",
                "--plugin", "drdynvc", "--data", "audin", "--"]
            address = self.lineEdit.text()
            username = self.lineEdit_2.text()
            password = self.lineEdit_3.text()

            if username and password:
                command.extend([
                    "-u", username,
                    "-p", "\"{0}\"".format(password)])

            if address:
                command.extend([address, "&"])
                code = subprocess.call(" ".join(command), shell=True)

            if code == 0:
                app = QApplication.instance()
                app.quit()
        except:
            pass

    def closeWindow(self, button):
        #关闭窗口
        app = QApplication.instance()
        app.quit()


class MyWindow(QMainWindow, Ui_RemoteConnect):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.pushButton.clicked.connect(myWin.connectTo)
    myWin.pushButton_2.clicked.connect(myWin.closeWindow)
    myWin.show()
    sys.exit(app.exec_())