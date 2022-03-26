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
    def __init__(self, controller: controller.Controller, list_widget: QListWidget = None):
        super().__init__()
        self.controller: controller.Controller = controller
        self.list_widget: QListWidget = list_widget

    finished = pyqtSignal()
    progress = pyqtSignal(int)
    recompiled = pyqtSignal(bool)

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
            self.add_to_list(smali_file)

        self.finished.emit()

    def run_recompile(self):
        self.recompiled.emit(self.controller.recompile_and_sign_apk())
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

        self.compareTableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.compareTableWidget.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.compareTableWidget.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)
        
        self.compareTableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # self.compareTableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)

        self.runtimeTableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.runtimeTableWidget.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        
        self.runtimeTableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # self.runtimeTableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)

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

        self.recompile_thread: QThread = QThread()
        self.recompile_worker_thread: Union[Worker, None] = None
        self.recompiled: bool = False
        self.recompile_loading_window: Union[QMessageBox, None] = None

    def apk_browse(self):
        file_path = QFileDialog.getOpenFileName(self, 'Open APK File', "", "Android Package File (*.apk)")
        # print(file_path[0])
        self.apkpathEdit.setText(file_path[0])

    def keystore_browse(self):
        key_path = QFileDialog.getOpenFileName(self, 'Open JKS File', "", "JKS File (*.jks)")
        # print(key_path[0])
        self.keystorePathEdit.setText(key_path[0])

    def obfuscate(self):        
        if self.apkpathEdit.text() != '' and "Zip archive data" in magic.from_file(self.apkpathEdit.text()):
            try:
                disassemble_time = time.process_time()
                obfuscate_time = time.process_time()
                time.sleep(2)

                # Get APK Hash
                before_hash_md5 = hashlib.md5()
                with open(self.apkpathEdit.text(),"rb") as f:
                    for byte_block in iter(lambda: f.read(4096), b""):
                        before_hash_md5.update(byte_block)

                before_hash_sha1 = hashlib.sha1()
                with open(self.apkpathEdit.text(),"rb") as f:
                    for byte_block in iter(lambda: f.read(4096), b""):
                        before_hash_sha1.update(byte_block)

                before_hash_sha256 = hashlib.sha256()
                with open(self.apkpathEdit.text(),"rb") as f:
                    for byte_block in iter(lambda: f.read(4096), b""):
                        before_hash_sha256.update(byte_block)
                
                # App Comparison Table
                self.compareTableWidget.insertRow(0)
                self.compareTableWidget.setItem(0, 0, QTableWidgetItem("MD5"))
                self.compareTableWidget.setItem(0, 1, QTableWidgetItem(before_hash_md5.hexdigest()))

                self.compareTableWidget.insertRow(1)
                self.compareTableWidget.setItem(1, 0, QTableWidgetItem("SHA1"))
                self.compareTableWidget.setItem(1, 1, QTableWidgetItem(before_hash_sha1.hexdigest()))

                self.compareTableWidget.insertRow(2)
                self.compareTableWidget.setItem(2, 0, QTableWidgetItem("SHA256"))
                self.compareTableWidget.setItem(2, 1, QTableWidgetItem(before_hash_sha256.hexdigest()))

                self.compareTableWidget.insertRow(3)
                self.compareTableWidget.setItem(3, 0, QTableWidgetItem("File Size"))
                self.compareTableWidget.setItem(3, 1, QTableWidgetItem(str(round(os.path.getsize(self.apkpathEdit.text()) / (1024 * 1024), 3)) + " MB"))

                # Runtime Table
                self.runtimeTableWidget.insertRow(0)
                self.runtimeTableWidget.setItem(0, 0, QTableWidgetItem("Disassembly Time"))
                self.runtimeTableWidget.setItem(0, 1, QTableWidgetItem(str(time.process_time() - disassemble_time)))

                self.runtimeTableWidget.insertRow(1)
                self.runtimeTableWidget.setItem(1, 0, QTableWidgetItem("Obfuscation Time"))
                self.runtimeTableWidget.setItem(1, 1, QTableWidgetItem(str(time.process_time() - obfuscate_time)))

                print(magic.from_file(self.apkpathEdit.text()))
                self.o = controller.Controller(self.apkpathEdit.text())
                self.worker_thread = Worker(self.o, self.listWidget)

                self.worker_thread.moveToThread(self.thread)
                self.thread.started.connect(self.worker_thread.run)
                self.worker_thread.finished.connect(self.thread.quit)
                self.worker_thread.finished.connect(self.all_done_window)
                self.worker_thread.finished.connect(self.worker_thread.deleteLater)
                self.thread.finished.connect(self.thread.deleteLater)
                self.worker_thread.progress.connect(self.increase_loading_bar)
                self.thread.start()

                self.progress_window()

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
        self.progress_window_canvas.setStandardButtons(QMessageBox.NoButton)
        self.progress_window_canvas.exec_()

    def all_done_window(self):
        self.progress_window_canvas.accept()
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

    '''def table_display(self):
        self.compareTableWidget.setRowCount(0)
        self.compareTableWidget.insertRow(self.compareTableWidget.rowCount())
        self.compareTableWidget.setItem(self.compareTableWidget.rowCount()-1, 0,
                                 QTableWidgetItem(self.listWidget.currentItem().text()))
        self.compareTableWidget.setItem(self.compareTableWidget.rowCount()-1, 1, QTableWidgetItem('before'))
        self.compareTableWidget.setItem(self.compareTableWidget.rowCount()-1, 2, QTableWidgetItem('after'))
    '''

    def compare_file(self):
        self.compare_box = QMessageBox()
        self.compare_box.setLayout(QHBoxLayout())
        
        self.compare_box.setStyleSheet(qdarkstyle.load_stylesheet())
        filelist = self.o.smali_files
        print(filelist[0])
        r = re.compile(f"\\\\{self.listWidget.currentItem().text()}")
        newlist = list(filter(r.match, filelist))
        with open(filelist[self.listWidget.currentRow()], 'r') as file:
            text = file.read().replace('\n', '')
        # self.compare_box.setText(text)
        self.compare_box.setWindowTitle(self.listWidget.currentItem().text())

        self.addCompareWidget()
        self.compare_box.exec_()

    def addCompareWidget(self):
        self.l = QHBoxLayout()
        self.before_text = QPlainTextEdit()
        self.after_text = QPlainTextEdit()

        self.before_text.appendPlainText("aaa")
        self.after_text.appendPlainText("bbb")

        self.l.addWidget(self.before_text)
        self.l.addWidget(self.after_text)
        
        self.compare_box.setLayout(self.l)

    def recompile_and_sign(self):
        if self.keystorePassEdit.text() != ''\
                and self.keystorePathEdit.text() != '':
            try:
                self.o.keystore_file = self.keystorePathEdit.text()
                self.o.keystore_passwd = self.keystorePassEdit.text()
                self.o.key_alias = self.keyaliasEdit.text()
                self.o.key_passwd = self.aliaspassEdit.text()

                self.recompile_worker_thread = Worker(self.o)
                self.recompile_worker_thread.moveToThread(self.recompile_thread)
                self.recompile_thread.started.connect(self.recompile_worker_thread.run_recompile)
                self.recompile_worker_thread.recompiled.connect(self.toggle_recompiled)
                self.recompile_worker_thread.finished.connect(self.recompile_thread.quit)
                self.recompile_worker_thread.finished.connect(self.recompile_done_window)
                self.recompile_thread.start()

                self.recompile_loading_window = QMessageBox()
                self.recompile_loading_window.setStyleSheet(qdarkstyle.load_stylesheet())
                self.recompile_loading_window.setStandardButtons(QMessageBox.NoButton)
                self.progress_window_canvas.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowTitleHint)
                self.recompile_loading_window.setWindowTitle("Loading")
                self.recompile_loading_window.setText("Build & Sign project files in progress...")
                self.recompile_loading_window.exec_()

            except Exception as e:
                print("Error: {0}".format(e))
                raise

        else:
            self.popup("Error", "Incorrect Keystore/Password Provided!")

    def toggle_recompiled(self, recompile_status: bool):
        self.recompiled = recompile_status

    def recompile_done_window(self):
        self.recompile_loading_window.accept()
        build_sign_message_box = QMessageBox()
        build_sign_message_box.setStyleSheet(qdarkstyle.load_stylesheet())
        build_sign_message_box.setStandardButtons(QMessageBox.Ok)

        if self.recompiled:
            build_sign_message_box.setWindowTitle("Build & Sign Success!")
            build_sign_message_box.setText(f"Successfully built and signed the obfuscated project files!\n"
                                           f"APK is located at {self.o.output_apk_path}")
        else:
            build_sign_message_box.setWindowTitle("Build & Sign Failed!")
            build_sign_message_box.setText("Unable to build and sign the obfuscated project files. "
                                           "Please double check your keystore inputs and try again.")

        build_sign_message_box.exec_()


def main():
    # You need one (and only one) QApplication instance per application.
    # Pass in sys.argv to allow command line arguments for your app.
    # If you know you won't use command line arguments QApplication([]) works too.
    app = QApplication()

    # Create a Qt widget, which will be our window.
    window = MainWindow()
    window.setWindowTitle("The Best Smali Obfuscator")
    window.show()  # IMPORTANT!!!!! Windows are hidden by default.

    # Start the event loop.
    app.exec_()


if __name__ == "__main__":
    main()

