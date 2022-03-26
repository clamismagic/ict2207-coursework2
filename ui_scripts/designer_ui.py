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
import time
import re

script_dir = os.path.dirname(__file__)
mymodule_dir = os.path.join(script_dir, '..', 'obfuscator_scripts')
sys.path.append(mymodule_dir)
import controller  # vscode


def exit_program():
    quit()


class Worker(QObject):
    def __init__(self, controller: controller.Controller, list_widget: QListWidget):
        super().__init__()
        self.controller: controller.Controller = controller
        self.list_widget: QListWidget = list_widget

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
            self.add_to_list(smali_file)

        self.finished.emit()

    def add_to_list(self, smali_file: str):
        self.list_widget.addItem(smali_file.rsplit("\\", 1)[1])


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.setStyleSheet(qdarkstyle.load_stylesheet())
        
        self.keystoreBrowseButton.clicked.connect(self.keystore_browse)
        self.listWidget.itemClicked.connect(self.compare_file)
        self.buildsignButton.clicked.connect(self.recompile_and_sign)

        # testing list
        # self.listWidget.addItem("aaaaaaa")
        # self.listWidget.addItem("bbbbbbb")

        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)
        
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.message_box: Union[QThread, None] = None

        self.thread: QThread = QThread()
        self.worker_thread: Union[Worker, None] = None
        self.o: Union[controller.Controller, None] = None

        self.actionExit.triggered.connect(exit_program)
        self.apkbrowseButton.clicked.connect(self.apk_browse)
        self.obfuscateButton.clicked.connect(self.obfuscate)

        self.files_obfuscated = 0
        self.progress_window_canvas: Union[QMessageBox, None] = None
        self.progress_bar_window: Union[QMessageBox, None] = None
        self.all_done_canvas: Union[QMessageBox, None] = None

        self.compare_box: Union[QMessageBox, None] = None

    def apk_browse(self):
        file_path = QFileDialog.getOpenFileName(self, 'Open APK File', "", "Android Package File (*.apk)")
        # print(file_path[0])
        self.apkpathEdit.setText(file_path[0])

    def keystore_browse(self):
        key_path = QFileDialog.getOpenFileName(self, 'Open JKS File', "", "JKS File (*.jks)")
        # print(key_path[0])
        self.keystorePathEdit.setText(key_path[0])

    def obfuscate(self):
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
                    for byte_block in iter(lambda: f.read(4096), b""):
                        before_hash.update(byte_block)
                
                self.tableWidget.insertRow(row_position)
                self.tableWidget.setItem(row_position, 0, QTableWidgetItem("SHA256"))
                self.tableWidget.setItem(row_position, 1, QTableWidgetItem(before_hash.hexdigest()))

                print(magic.from_file(self.apkpathEdit.text()))
                self.o = controller.Controller(self.apkpathEdit.text())
                self.worker_thread = Worker(self.o, self.listWidget)

                self.worker_thread.moveToThread(self.thread)
                self.thread.started.connect(self.worker_thread.run)
                self.worker_thread.finished.connect(self.thread.quit)
                self.worker_thread.finished.connect(self.worker_thread.deleteLater)
                self.thread.finished.connect(self.thread.deleteLater)
                self.worker_thread.progress.connect(self.increase_loading_bar)
                self.thread.start()

                self.progress_window()
                # self.worker_thread.finished.connect(self.progress_window_canvas.accept())
                # self.worker_thread.finished.connect(self.all_done_window())
                # self.listWidget.itemClicked.connect(self.table_display)

            except Exception as e:
                print("Error: {0}".format(e))
                raise

        else:
            self.popup("Error", "Incorrect File Provided!")

    def progress_window(self):
        self.progress_window_canvas = QMessageBox()
        self.progress_window_canvas.setStyleSheet(qdarkstyle.load_stylesheet())
        self.progress_window_canvas.setText("Number of files disassembled & obfuscated: 0")
        self.progress_window_canvas.setWindowTitle("Loading")
        self.progress_window_canvas.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowTitleHint)
        self.progress_window_canvas.setStandardButtons(QMessageBox.Ok)
        self.progress_window_canvas.exec_()

    def all_done_window(self):
        self.all_done_canvas = QMessageBox()
        self.all_done_canvas.setStyleSheet(qdarkstyle.load_stylesheet())
        self.all_done_canvas.setText(f"Disassembly and Obfuscation complete!\n"
                                     f"Total number of files decompiled & obfuscated: {self.files_obfuscated}")
        self.all_done_canvas.setWindowTitle("Completed")
        self.all_done_canvas.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowTitleHint)
        self.all_done_canvas.setStandardButtons(QMessageBox.Ok)
        self.all_done_canvas.exec_()

    def increase_loading_bar(self, inc: int):
        self.progress_window_canvas.setText("Number of files decompiled & obfuscated: " + str(inc))
        self.files_obfuscated = inc

    def popup(self, title, popup_message):
        self.message_box = QMessageBox()
        self.message_box.setStyleSheet(qdarkstyle.load_stylesheet())
        self.message_box.setWindowTitle(title)
        self.message_box.setText(popup_message)
        self.message_box.exec_()

    def table_display(self):
        self.tableWidget.setRowCount(0)
        self.tableWidget.insertRow(self.tableWidget.rowCount())
        self.tableWidget.setItem(self.tableWidget.rowCount()-1, 0,
                                 QTableWidgetItem(self.listWidget.currentItem().text()))
        self.tableWidget.setItem(self.tableWidget.rowCount()-1, 1, QTableWidgetItem('before'))
        self.tableWidget.setItem(self.tableWidget.rowCount()-1, 2, QTableWidgetItem('after'))

    def compare_file(self):
        self.compare_box = QMessageBox()
        # self.compare_box_layout = QHBoxLayout()
        # self.before_text = QPlainTextEdit()
        # self.after_text = QPlainTextEdit()

        # self.before_text.appendPlainText("aaa")
        # self.after_text.appendPlainText("bbb")
        
        self.compare_box.setStyleSheet(qdarkstyle.load_stylesheet())
        filelist = self.o.get_smali_files()
        print(filelist[0])
        r = re.compile(f"\\\\{self.listWidget.currentItem().text()}")
        newlist = list(filter(r.match, filelist))
        print(r)
        print(newlist)
        # self.compare_box.setLayout(self.compare_box_layout)
        with open(filelist[self.listWidget.currentRow()], 'r') as file:
            text = file.read().replace('\n', '')
        self.compare_box.setText(text)
        self.compare_box.setWindowTitle(self.listWidget.currentItem().text())
        # self.compare_box_layout.addWidget(self.before_text)
        # self.compare_box_layout.addWidget(self.after_text)
        self.compare_box.exec_()

    def recompile_and_sign(self):
        if self.keystorePassEdit.text() != ''\
                and self.keystorePathEdit.text() != ''\
                and self.aliaspassEdit.text() != ''\
                and self.keyaliasEdit.text() != '':
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

