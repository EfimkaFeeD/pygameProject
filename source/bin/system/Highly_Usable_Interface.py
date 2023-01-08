# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\game_launcher.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.project_label = QtWidgets.QLabel(self.centralwidget)
        self.project_label.setGeometry(QtCore.QRect(510, 0, 91, 81))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.project_label.setFont(font)
        self.project_label.setObjectName("project_label")
        self.zxc_label = QtWidgets.QLabel(self.centralwidget)
        self.zxc_label.setGeometry(QtCore.QRect(600, 0, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.zxc_label.setFont(font)
        self.zxc_label.setObjectName("zxc_label")
        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_button.setGeometry(QtCore.QRect(230, 150, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.start_button.setFont(font)
        self.start_button.setObjectName("start_button")
        self.quit_button = QtWidgets.QPushButton(self.centralwidget)
        self.quit_button.setGeometry(QtCore.QRect(230, 220, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.quit_button.setFont(font)
        self.quit_button.setObjectName("quit_button")
        self.bug_button = QtWidgets.QPushButton(self.centralwidget)
        self.bug_button.setGeometry(QtCore.QRect(440, 430, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.bug_button.setFont(font)
        self.bug_button.setObjectName("bug_button")
        self.git_button = QtWidgets.QPushButton(self.centralwidget)
        self.git_button.setGeometry(QtCore.QRect(40, 430, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.git_button.setFont(font)
        self.git_button.setObjectName("git_button")
        self.help_button = QtWidgets.QPushButton(self.centralwidget)
        self.help_button.setGeometry(QtCore.QRect(240, 430, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.help_button.setFont(font)
        self.help_button.setObjectName("help_button")
        self.launcher_label = QtWidgets.QLabel(self.centralwidget)
        self.launcher_label.setGeometry(QtCore.QRect(0, 0, 301, 71))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.launcher_label.setFont(font)
        self.launcher_label.setObjectName("launcher_label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.project_label.setText(_translate("MainWindow", "(project)"))
        self.zxc_label.setText(_translate("MainWindow", "zxc"))
        self.start_button.setText(_translate("MainWindow", "run"))
        self.quit_button.setText(_translate("MainWindow", "quit"))
        self.bug_button.setText(_translate("MainWindow", "bug reports"))
        self.git_button.setText(_translate("MainWindow", "our github"))
        self.help_button.setText(_translate("MainWindow", "help"))
        self.launcher_label.setText(_translate("MainWindow", " ZXC LAUNCHER"))