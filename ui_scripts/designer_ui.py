# import all for now
from email import message
from http.client import OK
from msilib.schema import ListView
from tkinter import E, Widget, messagebox
from tkinter.ttk import Treeview
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PyQt5.QtCore import QObject, QThread, pyqtSignal
from PySide2.QtGui import *
from PyQt5.QtGui import *
from obfuscator import Ui_MainWindow
from typing import List, Union
import os
import sys
import qdarkstyle
import magic
import threading
import hashlib

script_dir = os.path.dirname(__file__)
mymodule_dir = os.path.join(script_dir, '..', 'obfuscator_scripts')
sys.path.append(mymodule_dir)
import controller  # vscode


def exit_program():
    quit()


class Worker(QObject):
    def __init__(self, controller: controller.Controller):
        super().__init__()
        self.controller: controller.Controller = controller

    finished = pyqtSignal()
    progress = pyqtSignal(int)

    def run(self):
        # decompile apk into smali
        self.controller.disassemble_apk()

        # obfuscate smali files
        counter = 0
        self.controller.obfuscate_manifest()
        counter += 1
        self.progress.emit(counter)
        for smali_file in self.controller.smali_files:
            self.controller.obfuscate_smali(smali_file)
            counter += 1
            self.progress.emit(counter)
            print(f"counter: {counter}")

        self.finished.emit()


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.setStyleSheet(qdarkstyle.load_stylesheet())
        
        self.keystoreBrowseButton.clicked.connect(self.keystore_browse)
        self.listWidget.itemClicked.connect(self.tableDisplay)
        self.buildsignButton.clicked.connect(self.recompile_and_sign)

        # testing list
        # self.listWidget.addItem("aaaaaaa")
        # self.listWidget.addItem("bbbbbbb")

        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)
        
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)

        self.thread: QThread = QThread()
        self.worker_thread: Union[Worker, None] = None
        self.o: Union[controller.Controller, None] = None

        self.actionExit.triggered.connect(exit_program)
        self.apkbrowseButton.clicked.connect(self.apk_browse)
        self.obfuscateButton.clicked.connect(self.obfuscate)

    def apk_browse(self):
        file_path = QFileDialog.getOpenFileName(self, 'Open APK File', "", "Android Package File (*.apk)")
        # print(file_path[0])
        self.apkpathEdit.setText(file_path[0])

    def keystore_browse(self):
        key_path = QFileDialog.getOpenFileName(self, 'Open JKS File', "", "JKS File (*.jks)")
        # print(key_path[0])
        self.keystorePathEdit.setText(key_path[0])

    def obfuscate(self):
        # test = QMessageBox.information(self, 'Decompiling & Obfuscating...')
        # test.exec_()

        row_position = self.tableWidget.rowCount()

        # self.tableWidget.insertRow(row_position)
        # self.tableWidget.setItem(row_position, 0, QTableWidgetItem("category"))
        # self.tableWidget.setItem(row_position, 1, QTableWidgetItem("original"))
        # self.tableWidget.setItem(row_position, 2, QTableWidgetItem("obfuscated"))
        
        if self.apkpathEdit.text() != '' and "Zip archive data" in magic.from_file(self.apkpathEdit.text()):
            try:
                # get apk hash
                before_hash = hashlib.sha256()
                with open(self.apkpathEdit.text(),"rb") as f:
                    for byte_block in iter(lambda: f.read(4096),b""):
                        before_hash.update(byte_block)

                self.tableWidget.insertRow(row_position)
                self.tableWidget.setItem(row_position, 0, QTableWidgetItem("SHA256"))
                self.tableWidget.setItem(row_position, 1, QTableWidgetItem(before_hash.hexdigest()))

                print(magic.from_file(self.apkpathEdit.text()))
                self.o = controller.Controller(self.apkpathEdit.text())
                self.worker_thread = Worker(self.o)

                self.worker_thread.moveToThread(self.thread)
                self.thread.started.connect(self.worker_thread.run)
                self.worker_thread.finished.connect(self.thread.quit)
                self.worker_thread.finished.connect(self.worker_thread.deleteLater)
                self.thread.finished.connect(self.thread.deleteLater)
                self.worker_thread.progress.connect(self.increase_loading_bar)
                self.thread.start()
                
                self.add_to_list(self.o)
                # self.listWidget.itemClicked.connect(self.tableDisplay)

            except Exception as e:
                print("Error: {0}".format(e))
                raise

        else:
            self.popup("Error", "Incorrect File Provided!")

    def increase_loading_bar(self, inc: int):
        print(f"incrementing loading bar: {inc}")

    def popup(self, title, message):
        self.message_box = QMessageBox()
        self.message_box.setStyleSheet(qdarkstyle.load_stylesheet())
        self.message_box.setWindowTitle(title)
        self.message_box.setText(message)
        self.message_box.exec_()

    def add_to_list(self, o):
        for smali_file in o.get_smali_files():
            #self.listWidget.addItem(smali_file)
            self.listWidget.addItem(smali_file.rsplit("\\", 1)[1])

    def tableDisplay(self):
        self.tableWidget.setRowCount(0)
        self.tableWidget.insertRow(self.tableWidget.rowCount())
        self.tableWidget.setItem(self.tableWidget.rowCount()-1, 0, QTableWidgetItem(self.listWidget.currentItem().text()))
        self.tableWidget.setItem(self.tableWidget.rowCount()-1, 1, QTableWidgetItem('before'))
        self.tableWidget.setItem(self.tableWidget.rowCount()-1, 2, QTableWidgetItem('after'))

    def recompile_and_sign(self):
        if self.keystorePassEdit.text() != '' and self.keystorePathEdit.text() != '' and self.aliaspassEdit.text() != '' and self.keyaliasEdit.text() != '':
            try:
                print("test")
                self.o.recompile_and_sign_apk()
            except Exception as e:
                print("Error: {0}".format(e))
                raise

        else:
            self.popup("Error", "Incorrect Keystore/Password Provided!")


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
