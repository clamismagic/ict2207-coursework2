# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'obfuscator.ui'
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
        MainWindow.resize(1200, 800)
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 0, 1201, 41))
        self.titleHLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.titleHLayout.setObjectName(u"titleHLayout")
        self.titleHLayout.setContentsMargins(0, 0, 0, 0)
        self.titleLabel = QLabel(self.horizontalLayoutWidget)
        self.titleLabel.setObjectName(u"titleLabel")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.titleLabel.setFont(font)

        self.titleHLayout.addWidget(self.titleLabel)

        self.horizontalLayoutWidget_2 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(0, 40, 1201, 74))
        self.detailsHLayout = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.detailsHLayout.setObjectName(u"detailsHLayout")
        self.detailsHLayout.setContentsMargins(0, 0, 0, 0)
        self.detailsGLayout = QGridLayout()
        self.detailsGLayout.setObjectName(u"detailsGLayout")
        self.browseButton = QPushButton(self.horizontalLayoutWidget_2)
        self.browseButton.setObjectName(u"browseButton")

        self.detailsGLayout.addWidget(self.browseButton, 0, 2, 1, 2)

        self.apkpathEdit = QLineEdit(self.horizontalLayoutWidget_2)
        self.apkpathEdit.setObjectName(u"apkpathEdit")

        self.detailsGLayout.addWidget(self.apkpathEdit, 0, 1, 1, 1)

        self.apkpathLabel = QLabel(self.horizontalLayoutWidget_2)
        self.apkpathLabel.setObjectName(u"apkpathLabel")

        self.detailsGLayout.addWidget(self.apkpathLabel, 0, 0, 1, 1)

        self.obfuscateButton = QPushButton(self.horizontalLayoutWidget_2)
        self.obfuscateButton.setObjectName(u"obfuscateButton")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.obfuscateButton.sizePolicy().hasHeightForWidth())
        self.obfuscateButton.setSizePolicy(sizePolicy)
        self.obfuscateButton.setMinimumSize(QSize(140, 50))

        self.detailsGLayout.addWidget(self.obfuscateButton, 0, 4, 2, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.projectnameLabel = QLabel(self.horizontalLayoutWidget_2)
        self.projectnameLabel.setObjectName(u"projectnameLabel")

        self.detailsGLayout.addWidget(self.projectnameLabel, 1, 0, 1, 1)

        self.projectnameEdit = QLineEdit(self.horizontalLayoutWidget_2)
        self.projectnameEdit.setObjectName(u"projectnameEdit")

        self.detailsGLayout.addWidget(self.projectnameEdit, 1, 1, 1, 1)


        self.detailsHLayout.addLayout(self.detailsGLayout)

        self.horizontalLayoutWidget_3 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(0, 150, 1201, 451))
        self.textboxHLayout = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.textboxHLayout.setObjectName(u"textboxHLayout")
        self.textboxHLayout.setContentsMargins(0, 0, 0, 0)
        self.textboxGLayout = QGridLayout()
        self.textboxGLayout.setObjectName(u"textboxGLayout")
        self.textEdit = QTextEdit(self.horizontalLayoutWidget_3)
        self.textEdit.setObjectName(u"textEdit")

        self.textboxGLayout.addWidget(self.textEdit, 0, 0, 1, 1)

        self.textEdit_2 = QTextEdit(self.horizontalLayoutWidget_3)
        self.textEdit_2.setObjectName(u"textEdit_2")

        self.textboxGLayout.addWidget(self.textEdit_2, 0, 1, 1, 1)


        self.textboxHLayout.addLayout(self.textboxGLayout)

        self.horizontalLayoutWidget_4 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(0, 110, 1201, 41))
        self.tabHLayout = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.tabHLayout.setObjectName(u"tabHLayout")
        self.tabHLayout.setContentsMargins(0, 0, 0, 0)
        self.tabGLayout = QGridLayout()
        self.tabGLayout.setObjectName(u"tabGLayout")
        self.tabButtons = QPushButton(self.horizontalLayoutWidget_4)
        self.tabButtons.setObjectName(u"tabButtons")
        self.tabButtons.setMaximumSize(QSize(50, 16777215))

        self.tabGLayout.addWidget(self.tabButtons, 0, 0, 1, 1)


        self.tabHLayout.addLayout(self.tabGLayout)

        self.horizontalLayoutWidget_5 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(0, 600, 1201, 31))
        self.baHLayout = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.baHLayout.setObjectName(u"baHLayout")
        self.baHLayout.setContentsMargins(0, 0, 0, 0)
        self.baGLayout = QGridLayout()
        self.baGLayout.setObjectName(u"baGLayout")
        self.beforeLabel = QLabel(self.horizontalLayoutWidget_5)
        self.beforeLabel.setObjectName(u"beforeLabel")

        self.baGLayout.addWidget(self.beforeLabel, 0, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.afterLabel = QLabel(self.horizontalLayoutWidget_5)
        self.afterLabel.setObjectName(u"afterLabel")

        self.baGLayout.addWidget(self.afterLabel, 0, 1, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)


        self.baHLayout.addLayout(self.baGLayout)

        self.horizontalLayoutWidget_6 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_6.setObjectName(u"horizontalLayoutWidget_6")
        self.horizontalLayoutWidget_6.setGeometry(QRect(0, 630, 1201, 121))
        self.buildHLayout = QHBoxLayout(self.horizontalLayoutWidget_6)
        self.buildHLayout.setObjectName(u"buildHLayout")
        self.buildHLayout.setContentsMargins(0, 0, 0, 0)
        self.buildGLayout = QGridLayout()
        self.buildGLayout.setObjectName(u"buildGLayout")
        self.lineEdit_4 = QLineEdit(self.horizontalLayoutWidget_6)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.buildGLayout.addWidget(self.lineEdit_4, 1, 4, 1, 1)

        self.label_2 = QLabel(self.horizontalLayoutWidget_6)
        self.label_2.setObjectName(u"label_2")

        self.buildGLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.horizontalLayoutWidget_6)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(100, 70))

        self.buildGLayout.addWidget(self.pushButton_2, 0, 5, 2, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label = QLabel(self.horizontalLayoutWidget_6)
        self.label.setObjectName(u"label")

        self.buildGLayout.addWidget(self.label, 0, 0, 1, 1)

        self.lineEdit = QLineEdit(self.horizontalLayoutWidget_6)
        self.lineEdit.setObjectName(u"lineEdit")

        self.buildGLayout.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.lineEdit_2 = QLineEdit(self.horizontalLayoutWidget_6)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.buildGLayout.addWidget(self.lineEdit_2, 1, 1, 1, 2)

        self.pushButton = QPushButton(self.horizontalLayoutWidget_6)
        self.pushButton.setObjectName(u"pushButton")

        self.buildGLayout.addWidget(self.pushButton, 0, 2, 1, 1)

        self.lineEdit_3 = QLineEdit(self.horizontalLayoutWidget_6)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.buildGLayout.addWidget(self.lineEdit_3, 0, 4, 1, 1)

        self.label_3 = QLabel(self.horizontalLayoutWidget_6)
        self.label_3.setObjectName(u"label_3")

        self.buildGLayout.addWidget(self.label_3, 0, 3, 1, 1)

        self.label_4 = QLabel(self.horizontalLayoutWidget_6)
        self.label_4.setObjectName(u"label_4")

        self.buildGLayout.addWidget(self.label_4, 1, 3, 1, 1)


        self.buildHLayout.addLayout(self.buildGLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1200, 21))
        self.menuFiles = QMenu(self.menubar)
        self.menuFiles.setObjectName(u"menuFiles")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFiles.menuAction())
        self.menuFiles.addAction(self.actionExit)
        self.menuFiles.addSeparator()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.titleLabel.setText(QCoreApplication.translate("MainWindow", u"OBFUSCATOR TOOL", None))
        self.browseButton.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.apkpathLabel.setText(QCoreApplication.translate("MainWindow", u"APK Path: ", None))
        self.obfuscateButton.setText(QCoreApplication.translate("MainWindow", u"Obfuscate", None))
        self.projectnameLabel.setText(QCoreApplication.translate("MainWindow", u"Project Name: ", None))
        self.tabButtons.setText(QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.beforeLabel.setText(QCoreApplication.translate("MainWindow", u"Before", None))
        self.afterLabel.setText(QCoreApplication.translate("MainWindow", u"After", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Keystore Password: ", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Build & Sign", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Keystore Path: ", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Keystore Alias: ", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Alias Password: ", None))
        self.menuFiles.setTitle(QCoreApplication.translate("MainWindow", u"Files", None))
    # retranslateUi

