# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sps_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_sps(object):
    def setupUi(self, sps):
        sps.setObjectName("sps")
        sps.resize(441, 260)
        self.gridLayoutWidget = QtWidgets.QWidget(sps)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(60, 60, 301, 131))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButtonX = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButtonX.setObjectName("pushButtonX")
        self.gridLayout.addWidget(self.pushButtonX, 2, 0, 1, 1)
        self.pushButtonR = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButtonR.setObjectName("pushButtonR")
        self.gridLayout.addWidget(self.pushButtonR, 0, 0, 1, 1)
        self.pushButtonS = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButtonS.setObjectName("pushButtonS")
        self.gridLayout.addWidget(self.pushButtonS, 1, 0, 1, 1)
        self.lineEdit_R = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_R.setObjectName("lineEdit_R")
        self.gridLayout.addWidget(self.lineEdit_R, 0, 1, 1, 1)
        self.lineEdit_S = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_S.setObjectName("lineEdit_S")
        self.gridLayout.addWidget(self.lineEdit_S, 1, 1, 1, 1)
        self.lineEdit_X = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_X.setObjectName("lineEdit_X")
        self.gridLayout.addWidget(self.lineEdit_X, 2, 1, 1, 1)
        self.horizontalLayoutWidget = QtWidgets.QWidget(sps)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(60, 200, 301, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_sure = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_sure.setObjectName("pushButton_sure")
        self.horizontalLayout.addWidget(self.pushButton_sure)
        spacerItem = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_quit = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_quit.setObjectName("pushButton_quit")
        self.horizontalLayout.addWidget(self.pushButton_quit)

        self.retranslateUi(sps)
        QtCore.QMetaObject.connectSlotsByName(sps)

    def retranslateUi(self, sps):
        _translate = QtCore.QCoreApplication.translate
        sps.setWindowTitle(_translate("sps", "选择sps"))
        self.pushButtonX.setText(_translate("sps", "选择"))
        self.pushButtonR.setText(_translate("sps", "选择"))
        self.pushButtonS.setText(_translate("sps", "选择"))
        self.lineEdit_R.setText(_translate("sps", "请选择R文件"))
        self.lineEdit_S.setText(_translate("sps", "请选择S文件"))
        self.lineEdit_X.setText(_translate("sps", "请选择X文件"))
        self.pushButton_sure.setText(_translate("sps", "确定"))
        self.pushButton_quit.setText(_translate("sps", "退出"))

