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
        self.detailsHLayout = QHBoxLayout()
        self.detailsHLayout.setObjectName(u"detailsHLayout")
        self.detailsGLayout = QGridLayout()
        self.detailsGLayout.setObjectName(u"detailsGLayout")
        self.apkbrowseButton = QPushButton(self.centralwidget)
        self.apkbrowseButton.setObjectName(u"apkbrowseButton")
        self.apkbrowseButton.setMinimumSize(QSize(75, 23))

        self.detailsGLayout.addWidget(self.apkbrowseButton, 0, 3, 1, 2)

        self.projectnameEdit = QLineEdit(self.centralwidget)
        self.projectnameEdit.setObjectName(u"projectnameEdit")

        self.detailsGLayout.addWidget(self.projectnameEdit, 1, 1, 1, 1)

        self.projectnameLabel = QLabel(self.centralwidget)
        self.projectnameLabel.setObjectName(u"projectnameLabel")

        self.detailsGLayout.addWidget(self.projectnameLabel, 1, 0, 1, 1)

        self.apkpathEdit = QLineEdit(self.centralwidget)
        self.apkpathEdit.setObjectName(u"apkpathEdit")
        self.apkpathEdit.setReadOnly(True)

        self.detailsGLayout.addWidget(self.apkpathEdit, 0, 1, 1, 1)

        self.obfuscateButton = QPushButton(self.centralwidget)
        self.obfuscateButton.setObjectName(u"obfuscateButton")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.obfuscateButton.sizePolicy().hasHeightForWidth())
        self.obfuscateButton.setSizePolicy(sizePolicy)
        self.obfuscateButton.setMinimumSize(QSize(140, 50))

        self.detailsGLayout.addWidget(self.obfuscateButton, 0, 5, 2, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.verifyapkButton = QPushButton(self.centralwidget)
        self.verifyapkButton.setObjectName(u"verifyapkButton")
        self.verifyapkButton.setMinimumSize(QSize(75, 23))

        self.detailsGLayout.addWidget(self.verifyapkButton, 0, 2, 1, 1)

        self.apkpathLabel = QLabel(self.centralwidget)
        self.apkpathLabel.setObjectName(u"apkpathLabel")

        self.detailsGLayout.addWidget(self.apkpathLabel, 0, 0, 1, 1)


        self.detailsHLayout.addLayout(self.detailsGLayout)


        self.verticalLayout.addLayout(self.detailsHLayout)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.comparisonmetricsLabel = QLabel(self.centralwidget)
        self.comparisonmetricsLabel.setObjectName(u"comparisonmetricsLabel")
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.comparisonmetricsLabel.setFont(font)

        self.gridLayout.addWidget(self.comparisonmetricsLabel, 0, 1, 1, 1)

        self.changedfilesLabel = QLabel(self.centralwidget)
        self.changedfilesLabel.setObjectName(u"changedfilesLabel")
        font1 = QFont()
        font1.setPointSize(8)
        font1.setBold(True)
        font1.setWeight(75)
        self.changedfilesLabel.setFont(font1)

        self.gridLayout.addWidget(self.changedfilesLabel, 0, 0, 1, 1)

        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setObjectName(u"listWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy1)
        self.listWidget.setStyleSheet(u"QListWidget::item { border-bottom: 1px solid gray; opacity: 0.5; padding-top: 5px; padding-bottom: 5px; }")

        self.gridLayout.addWidget(self.listWidget, 1, 0, 1, 1)

        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(5)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.tableView, 1, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.buildHLayout = QHBoxLayout()
        self.buildHLayout.setObjectName(u"buildHLayout")
        self.buildGLayout = QGridLayout()
        self.buildGLayout.setObjectName(u"buildGLayout")
        self.keyaliasEdit = QLineEdit(self.centralwidget)
        self.keyaliasEdit.setObjectName(u"keyaliasEdit")

        self.buildGLayout.addWidget(self.keyaliasEdit, 0, 4, 1, 1)

        self.aliaspassLabel = QLabel(self.centralwidget)
        self.aliaspassLabel.setObjectName(u"aliaspassLabel")

        self.buildGLayout.addWidget(self.aliaspassLabel, 1, 3, 1, 1)

        self.keyaliasLabel = QLabel(self.centralwidget)
        self.keyaliasLabel.setObjectName(u"keyaliasLabel")

        self.buildGLayout.addWidget(self.keyaliasLabel, 0, 3, 1, 1)

        self.keystoreBrowseButton = QPushButton(self.centralwidget)
        self.keystoreBrowseButton.setObjectName(u"keystoreBrowseButton")
        self.keystoreBrowseButton.setMinimumSize(QSize(75, 23))

        self.buildGLayout.addWidget(self.keystoreBrowseButton, 0, 2, 1, 1)

        self.verifykeyButton = QPushButton(self.centralwidget)
        self.verifykeyButton.setObjectName(u"verifykeyButton")
        self.verifykeyButton.setMinimumSize(QSize(100, 70))

        self.buildGLayout.addWidget(self.verifykeyButton, 0, 5, 2, 1)

        self.keypassLabel = QLabel(self.centralwidget)
        self.keypassLabel.setObjectName(u"keypassLabel")

        self.buildGLayout.addWidget(self.keypassLabel, 1, 0, 1, 1)

        self.keystorePathEdit = QLineEdit(self.centralwidget)
        self.keystorePathEdit.setObjectName(u"keystorePathEdit")

        self.buildGLayout.addWidget(self.keystorePathEdit, 0, 1, 1, 1)

        self.keypathLabel = QLabel(self.centralwidget)
        self.keypathLabel.setObjectName(u"keypathLabel")

        self.buildGLayout.addWidget(self.keypathLabel, 0, 0, 1, 1)

        self.aliaspassEdit = QLineEdit(self.centralwidget)
        self.aliaspassEdit.setObjectName(u"aliaspassEdit")

        self.buildGLayout.addWidget(self.aliaspassEdit, 1, 4, 1, 1)

        self.buildsignButton = QPushButton(self.centralwidget)
        self.buildsignButton.setObjectName(u"buildsignButton")
        self.buildsignButton.setMinimumSize(QSize(100, 70))

        self.buildGLayout.addWidget(self.buildsignButton, 0, 6, 2, 1)

        self.keystorePassEdit = QLineEdit(self.centralwidget)
        self.keystorePassEdit.setObjectName(u"keystorePassEdit")

        self.buildGLayout.addWidget(self.keystorePassEdit, 1, 1, 1, 2)


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
        self.apkbrowseButton.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.projectnameLabel.setText(QCoreApplication.translate("MainWindow", u"Project Name: ", None))
        self.obfuscateButton.setText(QCoreApplication.translate("MainWindow", u"Obfuscate", None))
        self.verifyapkButton.setText(QCoreApplication.translate("MainWindow", u"Verify", None))
        self.apkpathLabel.setText(QCoreApplication.translate("MainWindow", u"APK Path: ", None))
        self.comparisonmetricsLabel.setText(QCoreApplication.translate("MainWindow", u"Comparison Metrics", None))
        self.changedfilesLabel.setText(QCoreApplication.translate("MainWindow", u"List of Changed Files", None))
        self.aliaspassLabel.setText(QCoreApplication.translate("MainWindow", u"Alias Password: ", None))
        self.keyaliasLabel.setText(QCoreApplication.translate("MainWindow", u"Keystore Alias: ", None))
        self.keystoreBrowseButton.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.verifykeyButton.setText(QCoreApplication.translate("MainWindow", u"Verify", None))
        self.keypassLabel.setText(QCoreApplication.translate("MainWindow", u"Keystore Password: ", None))
        self.keypathLabel.setText(QCoreApplication.translate("MainWindow", u"Keystore Path: ", None))
        self.buildsignButton.setText(QCoreApplication.translate("MainWindow", u"Build and Sign", None))
        self.menuFiles.setTitle(QCoreApplication.translate("MainWindow", u"Files", None))
    # retranslateUi

