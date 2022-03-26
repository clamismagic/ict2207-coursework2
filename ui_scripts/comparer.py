# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'comparer.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(854, 688)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.beforeLabel = QLabel(self.centralwidget)
        self.beforeLabel.setObjectName(u"beforeLabel")
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.beforeLabel.setFont(font)
        self.beforeLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.beforeLabel, 0, 0, 1, 1)

        self.afterLabel = QLabel(self.centralwidget)
        self.afterLabel.setObjectName(u"afterLabel")
        self.afterLabel.setFont(font)
        self.afterLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.afterLabel, 0, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.beforeEdit = QTextEdit(self.centralwidget)
        self.beforeEdit.setObjectName(u"beforeEdit")
        self.beforeEdit.setReadOnly(True)

        self.horizontalLayout.addWidget(self.beforeEdit)

        self.afterEdit = QTextEdit(self.centralwidget)
        self.afterEdit.setObjectName(u"afterEdit")
        self.afterEdit.setReadOnly(True)

        self.horizontalLayout.addWidget(self.afterEdit)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 2)

        self.popoutOkButton = QPushButton(self.centralwidget)
        self.popoutOkButton.setObjectName(u"popoutOkButton")

        self.gridLayout.addWidget(self.popoutOkButton, 2, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Comparing Code", None))
        self.beforeLabel.setText(QCoreApplication.translate("MainWindow", u"Original", None))
        self.afterLabel.setText(QCoreApplication.translate("MainWindow", u"Obfuscated", None))
        self.popoutOkButton.setText(QCoreApplication.translate("MainWindow", u"Ok", None))
    # retranslateUi

