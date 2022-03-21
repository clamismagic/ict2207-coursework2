# import all for now
from email import message
from http.client import OK
from tkinter import E, Widget, messagebox
from tkinter.ttk import Treeview
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PyQt5.uic import loadUi
from PyQt5.QtGui import *
from obfuscator import Ui_MainWindow
from obfuscator_scripts import controller
import os
import sys
import qdarkstyle
import magic

script_dir = os.path.dirname(__file__)
mymodule_dir = os.path.join(script_dir, '..', 'obfuscator_scripts')
sys.path.append(mymodule_dir)


def exit_program():
    quit()


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.setStyleSheet(qdarkstyle.load_stylesheet())

        self.actionExit.triggered.connect(exit_program)
        self.apkbrowseButton.clicked.connect(self.apk_browse)
        self.obfuscateButton.clicked.connect(self.obfuscate)
        self.keystoreBrowseButton.clicked.connect(self.keystore_browse)
        
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)

    def apk_browse(self):
        file_path = QFileDialog.getOpenFileName(self, 'Open APK File', "", "Android Package File (*.apk)")
        # print(file_path[0])
        self.apkpathEdit.setText(file_path[0])

    def keystore_browse(self):
        key_path = QFileDialog.getOpenFileName(self, 'Open JKS File', "", "JKS File (*.jks)")
        # print(key_path[0])
        self.keystorePathEdit.setText(key_path[0])

    def obfuscate(self):
        # self.listWidget.addItem("abc") # add items
        rowPosition = self.tableWidget.rowCount()

        self.tableWidget.insertRow(rowPosition)
        self.tableWidget.insertRow(rowPosition)
        self.tableWidget.insertRow(rowPosition)

        self.tableWidget.setItem(rowPosition, 0, QTableWidgetItem("hash"))
        self.tableWidget.setItem(rowPosition, 1, QTableWidgetItem("1234"))
        self.tableWidget.setItem(rowPosition, 2, QTableWidgetItem("4321"))

        """data = {'col1':['1','2','3','4'], 'col2':['1','2','1','3'], 'col3':['1','1','2','1']}
        
        horHeaders = []
        for n, key in enumerate(sorted(data.keys())):
            horHeaders.append(key)
            for m, item in enumerate(data[key]):
                newitem = QTableWidgetItem(item)
                self.tableWidget.setItem(m, n, newitem)
        self.tableWidget.setHorizontalHeaderLabels(horHeaders)
        
        self.tableWidget(12, 3, self)
        table = QTableView(self.tableWidget)"""
        
        print(magic.from_file(self.apkpathEdit.text()))
        
        if self.apkpathEdit.text() != '' and "Zip archive data" in magic.from_file(self.apkpathEdit.text()):
            try:
                o = controller.Controller(self.apkpathEdit.text())
                
            except Exception as e:
                print("Error: {0}".format(e))
                raise

        else:
            self.popup("Error", "Incorrect File Provided!")

    def popup(title, message):
        message_box = QMessageBox()
        message_box.setStyleSheet(qdarkstyle.load_stylesheet())
        message_box.setWindowTitle(title)
        message_box.setText(message)
        message_box.exec_()


def main():
    # You need one (and only one) QApplication instance per application.
    # Pass in sys.argv to allow command line arguments for your app.
    # If you know you won't use command line arguments QApplication([]) works too.
    app = QApplication()

    # Create a Qt widget, which will be our window.
    window = MainWindow()
    window.show()  # IMPORTANT!!!!! Windows are hidden by default.

    # Start the event loop.
    app.exec_()


if __name__ == "__main__":
    main()
