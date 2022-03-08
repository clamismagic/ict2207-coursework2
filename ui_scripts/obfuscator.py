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
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.titleHLayout = QHBoxLayout()
        self.titleHLayout.setObjectName(u"titleHLayout")
        self.titleLabel = QLabel(self.centralwidget)
        self.titleLabel.setObjectName(u"titleLabel")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.titleLabel.setFont(font)

        self.titleHLayout.addWidget(self.titleLabel)


        self.verticalLayout.addLayout(self.titleHLayout)

        self.detailsHLayout = QHBoxLayout()
        self.detailsHLayout.setObjectName(u"detailsHLayout")
        self.detailsGLayout = QGridLayout()
        self.detailsGLayout.setObjectName(u"detailsGLayout")
        self.apkbrowseButton = QPushButton(self.centralwidget)
        self.apkbrowseButton.setObjectName(u"apkbrowseButton")

        self.detailsGLayout.addWidget(self.apkbrowseButton, 0, 2, 1, 2)

        self.apkpathEdit = QLineEdit(self.centralwidget)
        self.apkpathEdit.setObjectName(u"apkpathEdit")

        self.detailsGLayout.addWidget(self.apkpathEdit, 0, 1, 1, 1)

        self.apkpathLabel = QLabel(self.centralwidget)
        self.apkpathLabel.setObjectName(u"apkpathLabel")

        self.detailsGLayout.addWidget(self.apkpathLabel, 0, 0, 1, 1)

        self.obfuscateButton = QPushButton(self.centralwidget)
        self.obfuscateButton.setObjectName(u"obfuscateButton")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.obfuscateButton.sizePolicy().hasHeightForWidth())
        self.obfuscateButton.setSizePolicy(sizePolicy)
        self.obfuscateButton.setMinimumSize(QSize(140, 50))

        self.detailsGLayout.addWidget(self.obfuscateButton, 0, 4, 2, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.projectnameLabel = QLabel(self.centralwidget)
        self.projectnameLabel.setObjectName(u"projectnameLabel")

        self.detailsGLayout.addWidget(self.projectnameLabel, 1, 0, 1, 1)

        self.projectnameEdit = QLineEdit(self.centralwidget)
        self.projectnameEdit.setObjectName(u"projectnameEdit")

        self.detailsGLayout.addWidget(self.projectnameEdit, 1, 1, 1, 1)


        self.detailsHLayout.addLayout(self.detailsGLayout)


        self.verticalLayout.addLayout(self.detailsHLayout)

        self.tabHLayout = QHBoxLayout()
        self.tabHLayout.setObjectName(u"tabHLayout")
        self.tabGLayout = QGridLayout()
        self.tabGLayout.setObjectName(u"tabGLayout")
        self.tabButtons = QPushButton(self.centralwidget)
        self.tabButtons.setObjectName(u"tabButtons")
        self.tabButtons.setMaximumSize(QSize(50, 16777215))

        self.tabGLayout.addWidget(self.tabButtons, 0, 0, 1, 1)


        self.tabHLayout.addLayout(self.tabGLayout)


        self.verticalLayout.addLayout(self.tabHLayout)

        self.textboxHLayout = QHBoxLayout()
        self.textboxHLayout.setObjectName(u"textboxHLayout")
        self.textboxGLayout = QGridLayout()
        self.textboxGLayout.setObjectName(u"textboxGLayout")
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")

        self.textboxGLayout.addWidget(self.textEdit, 0, 0, 1, 1)

        self.textEdit_2 = QTextEdit(self.centralwidget)
        self.textEdit_2.setObjectName(u"textEdit_2")

        self.textboxGLayout.addWidget(self.textEdit_2, 0, 1, 1, 1)


        self.textboxHLayout.addLayout(self.textboxGLayout)


        self.verticalLayout.addLayout(self.textboxHLayout)

        self.baHLayout = QHBoxLayout()
        self.baHLayout.setObjectName(u"baHLayout")
        self.baGLayout = QGridLayout()
        self.baGLayout.setObjectName(u"baGLayout")
        self.beforeLabel = QLabel(self.centralwidget)
        self.beforeLabel.setObjectName(u"beforeLabel")

        self.baGLayout.addWidget(self.beforeLabel, 0, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.afterLabel = QLabel(self.centralwidget)
        self.afterLabel.setObjectName(u"afterLabel")

        self.baGLayout.addWidget(self.afterLabel, 0, 1, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)


        self.baHLayout.addLayout(self.baGLayout)


        self.verticalLayout.addLayout(self.baHLayout)

        self.buildHLayout = QHBoxLayout()
        self.buildHLayout.setObjectName(u"buildHLayout")
        self.buildGLayout = QGridLayout()
        self.buildGLayout.setObjectName(u"buildGLayout")
        self.lineEdit_4 = QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.buildGLayout.addWidget(self.lineEdit_4, 1, 4, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.buildGLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(100, 70))

        self.buildGLayout.addWidget(self.pushButton_2, 0, 5, 2, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.buildGLayout.addWidget(self.label, 0, 0, 1, 1)

        self.keystorePathEdit = QLineEdit(self.centralwidget)
        self.keystorePathEdit.setObjectName(u"keystorePathEdit")

        self.buildGLayout.addWidget(self.keystorePathEdit, 0, 1, 1, 1)

        self.keystorePasswordEdit = QLineEdit(self.centralwidget)
        self.keystorePasswordEdit.setObjectName(u"keystorePasswordEdit")

        self.buildGLayout.addWidget(self.keystorePasswordEdit, 1, 1, 1, 2)

        self.keystoreBrowseButton = QPushButton(self.centralwidget)
        self.keystoreBrowseButton.setObjectName(u"keystoreBrowseButton")

        self.buildGLayout.addWidget(self.keystoreBrowseButton, 0, 2, 1, 1)

        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.buildGLayout.addWidget(self.lineEdit_3, 0, 4, 1, 1)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.buildGLayout.addWidget(self.label_3, 0, 3, 1, 1)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.buildGLayout.addWidget(self.label_4, 1, 3, 1, 1)


        self.buildHLayout.addLayout(self.buildGLayout)


        self.verticalLayout.addLayout(self.buildHLayout)

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
        self.apkbrowseButton.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.apkpathLabel.setText(QCoreApplication.translate("MainWindow", u"APK Path: ", None))
        self.obfuscateButton.setText(QCoreApplication.translate("MainWindow", u"Obfuscate", None))
        self.projectnameLabel.setText(QCoreApplication.translate("MainWindow", u"Project Name: ", None))
        self.tabButtons.setText(QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.beforeLabel.setText(QCoreApplication.translate("MainWindow", u"Before", None))
        self.afterLabel.setText(QCoreApplication.translate("MainWindow", u"After", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Keystore Password: ", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Build & Sign", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Keystore Path: ", None))
        self.keystoreBrowseButton.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Keystore Alias: ", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Alias Password: ", None))
        self.menuFiles.setTitle(QCoreApplication.translate("MainWindow", u"Files", None))
    # retranslateUi

