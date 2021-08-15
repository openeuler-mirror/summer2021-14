import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
#from remoteconnect import *
from PyQt5 import QtCore, QtGui, QtWidgets
import subprocess

class Ui_RemoteConnect(object):
    def setupUi(self, RemoteConnect):
        RemoteConnect.setObjectName("RemoteConnect")
        RemoteConnect.resize(549, 377)
        self.pushButton = QtWidgets.QPushButton(RemoteConnect)
        self.pushButton.setGeometry(QtCore.QRect(70, 280, 121, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(RemoteConnect)
        self.pushButton_2.setGeometry(QtCore.QRect(350, 280, 121, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit = QtWidgets.QLineEdit(RemoteConnect)
        self.lineEdit.setGeometry(QtCore.QRect(150, 90, 271, 31))
        self.lineEdit.setPlaceholderText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(RemoteConnect)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 150, 271, 31))
        self.lineEdit_2.setPlaceholderText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(RemoteConnect)
        self.lineEdit_3.setGeometry(QtCore.QRect(150, 210, 271, 31))
        self.lineEdit_3.setPlaceholderText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label = QtWidgets.QLabel(RemoteConnect)
        self.label.setGeometry(QtCore.QRect(60, 100, 54, 12))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(RemoteConnect)
        self.label_2.setGeometry(QtCore.QRect(60, 160, 54, 12))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(RemoteConnect)
        self.label_3.setGeometry(QtCore.QRect(60, 220, 54, 12))
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
        #self.pushButton.clicked.connect(connectTo)
        #self.pushButton_2.clicked.connect(closeWindow)



    def connectTo(self, button):
        """
        Attempt to connect using the user input.
        """

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
            '''
            address = Ui_RemoteConnect.retranslateUi.lineEdit.text()
            username = Ui_RemoteConnect.retranslateUi.lineEdit2.text()
            password = Ui_RemoteConnect.retranslateUi.lineEdit3.text()
            
            print(address)
            print(username)
            print(password)
            '''
            # If the username and password are present then use them.
            if username and password:
                command.extend([
                    "-u", username,
                    "-p", "\"{0}\"".format(password)])

            # If an address is present attempt to connect.
            if address:
                command.extend([address, "&"])
                code = subprocess.call(" ".join(command), shell=True)

            # Check the return code (if any) and close on success.
            if code == 0:
                app = QApplication.instance()
                # 退出应用程序
                app.quit()
        except:
            pass

    def closeWindow(self, button):
        """
        Close the window and end the program.
        """
        app = QApplication.instance()
        # 退出应用程序
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
