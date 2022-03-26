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
from comparer import Ui_MainWindow as popout
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

mutex = threading.Lock()


def exit_program():
    quit()


class Worker(QObject):
    def __init__(self, controller: controller.Controller, list_widget: QListWidget = None):
        super().__init__()
        self.controller: controller.Controller = controller
        self.list_widget: QListWidget = list_widget

    finished = pyqtSignal()
    decompiled = pyqtSignal()
    disassemble_time_taken = pyqtSignal(float)
    obfuscate_time_taken = pyqtSignal(float)
    recompile_time_taken = pyqtSignal(float)
    progress = pyqtSignal(int)
    recompiled = pyqtSignal(bool)

    def run(self):
        global mutex

        # decompile apk into smali
        start_disassembly = time.time()
        self.controller.disassemble_apk()
        self.disassemble_time_taken.emit(time.time() - start_disassembly)
        self.decompiled.emit()

        # allow main thread to read files
        mutex.acquire()
        print("OBFUSCATING FILES")

        # obfuscate smali files
        start_obfuscation = time.time()
        counter = 0
        self.controller.obfuscate_manifest()
        self.add_to_list(self.controller.manifest_file)
        counter += 1
        self.progress.emit(counter)
        for smali_file in self.controller.smali_files:
            self.controller.obfuscate_smali(smali_file)
            counter += 1
            self.progress.emit(counter)
            self.add_to_list(smali_file)

        self.obfuscate_time_taken.emit(time.time() - start_obfuscation)
        self.finished.emit()
        mutex.release()

    def run_recompile(self):
        recompile_start_time = time.time()
        self.recompiled.emit(self.controller.recompile_and_sign_apk())
        self.recompile_time_taken.emit(time.time() - recompile_start_time)
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

        self.original_smali: List[str] = []
        self.obfuscated_smali: List[str] = []
        self.files_obfuscated = 0
        self.progress_window_canvas: Union[QMessageBox, None] = None
        self.progress_bar_window: Union[QMessageBox, None] = None
        self.all_done_canvas: Union[QMessageBox, None] = None
        self.disassemble_time_taken: float = 0
        self.obfuscate_time_taken: float = 0

        self.compare_box: Union[QMessageBox, None] = None

        self.recompile_thread: QThread = QThread()
        self.recompile_worker_thread: Union[Worker, None] = None
        self.recompiled: bool = False
        self.recompile_time_taken: float = 0
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
        global mutex
        if self.apkpathEdit.text() != '' and "Zip archive data" in magic.from_file(self.apkpathEdit.text()):
            try:
                disassemble_time = time.process_time()
                obfuscate_time = time.process_time()

                # Get APK Hash
                before_hash_md5 = hashlib.md5()
                with open(self.apkpathEdit.text(), "rb") as f:
                    for byte_block in iter(lambda: f.read(4096), b""):
                        before_hash_md5.update(byte_block)

                before_hash_sha1 = hashlib.sha1()
                with open(self.apkpathEdit.text(), "rb") as f:
                    for byte_block in iter(lambda: f.read(4096), b""):
                        before_hash_sha1.update(byte_block)

                before_hash_sha256 = hashlib.sha256()
                with open(self.apkpathEdit.text(), "rb") as f:
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
                self.compareTableWidget.setItem(3,
                                                1,
                                                QTableWidgetItem(str(
                                                    round(os.path.getsize(
                                                        self.apkpathEdit.text()) / (1024 * 1024), 3)) + " MB"))

                # Runtime Table
                self.runtimeTableWidget.insertRow(0)
                self.runtimeTableWidget.setItem(0, 0, QTableWidgetItem("Disassembly Time"))

                self.runtimeTableWidget.insertRow(1)
                self.runtimeTableWidget.setItem(1, 0, QTableWidgetItem("Obfuscation Time"))

                self.runtimeTableWidget.insertRow(2)
                self.runtimeTableWidget.setItem(2, 0, QTableWidgetItem("Recompile Time"))

                print(magic.from_file(self.apkpathEdit.text()))
                self.o = controller.Controller(self.apkpathEdit.text())
                self.worker_thread = Worker(self.o, self.listWidget)

                self.worker_thread.moveToThread(self.thread)
                self.thread.started.connect(self.worker_thread.run)
                mutex.acquire()
                self.worker_thread.decompiled.connect(self.get_original_files)
                self.worker_thread.disassemble_time_taken.connect(self.get_disassemble_time_taken)
                self.worker_thread.obfuscate_time_taken.connect(self.get_obfuscate_time_taken)
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

    def get_original_files(self):
        print("PRINTING ORIGINAL FILES")
        with open(self.o.manifest_file, 'r') as file:
            self.original_smali.append(file.read())
        for smali_file in self.o.smali_files:
            with open(smali_file, 'r') as file:
                self.original_smali.append(file.read())
        mutex.release()

    def get_disassemble_time_taken(self, time_taken: float):
        self.disassemble_time_taken = time_taken

    def get_obfuscate_time_taken(self, time_taken: float):
        self.obfuscate_time_taken = time_taken

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
        self.runtimeTableWidget.setItem(0, 1, QTableWidgetItem(f"{str(self.disassemble_time_taken)} seconds"))
        self.runtimeTableWidget.setItem(1, 1, QTableWidgetItem(f"{str(self.obfuscate_time_taken)} seconds"))

        # grab contents of obfuscated files
        with open(self.o.manifest_file, 'r') as file:
            self.obfuscated_smali.append(file.read())
        for smali_file in self.o.smali_files:
            with open(smali_file, 'r') as file:
                self.obfuscated_smali.append(file.read())

    def increase_loading_bar(self, inc: int):
        self.progress_window_canvas.setText("Number of files decompiled & obfuscated: " + str(inc))
        self.files_obfuscated = inc

    def popup(self, title, popup_message):
        self.message_box = QMessageBox()
        self.message_box.setStyleSheet(qdarkstyle.load_stylesheet())
        self.message_box.setWindowTitle(title)
        self.message_box.setText(popup_message)
        self.message_box.exec_()

    def compare_file(self):
        before_text = self.original_smali[self.listWidget.currentRow()]
        after_text = self.obfuscated_smali[self.listWidget.currentRow()]

        self.compare_box = ListPopUp(before_text, after_text)
        self.compare_box.show()

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
                self.recompile_worker_thread.recompile_time_taken.connect(self.get_recompile_time_taken)
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

    def get_recompile_time_taken(self, time_taken: float):
        self.recompile_time_taken = time_taken

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
            
            # Get APK Hash
            after_hash_md5 = hashlib.md5()
            with open(self.o.output_apk_path, "rb") as f:
                for byte_block in iter(lambda: f.read(4096), b""):
                    after_hash_md5.update(byte_block)

            after_hash_sha1 = hashlib.sha1()
            with open(self.o.output_apk_path, "rb") as f:
                for byte_block in iter(lambda: f.read(4096), b""):
                    after_hash_sha1.update(byte_block)

            after_hash_sha256 = hashlib.sha256()
            with open(self.o.output_apk_path, "rb") as f:
                for byte_block in iter(lambda: f.read(4096), b""):
                    after_hash_sha256.update(byte_block)
            
            # App Comparison Table
            self.compareTableWidget.setItem(0, 2, QTableWidgetItem(after_hash_md5.hexdigest()))
            self.compareTableWidget.setItem(1, 2, QTableWidgetItem(after_hash_sha1.hexdigest()))
            self.compareTableWidget.setItem(2, 2, QTableWidgetItem(after_hash_sha256.hexdigest()))
            self.compareTableWidget.setItem(3,
                                            2,
                                            QTableWidgetItem(
                                                str(round(os.path.getsize(
                                                    self.o.output_apk_path) / (1024 * 1024), 3)) + " MB"))
            self.runtimeTableWidget.setItem(2, 1, QTableWidgetItem(f"{str(self.recompile_time_taken)} seconds"))
            os.startfile(os.path.dirname(self.o.output_apk_path))
        else:
            build_sign_message_box.setWindowTitle("Build & Sign Failed!")
            build_sign_message_box.setText("Unable to build and sign the obfuscated project files. "
                                           "Please double check your keystore inputs and try again.")

        build_sign_message_box.exec_()


class ListPopUp(QMainWindow, popout):
    def __init__(self, before_text: str, after_text: str,):
        super().__init__()
        self.setupUi(self)
        self.before_text: str = before_text
        self.after_text: str = after_text
        self.beforeEdit.setText(before_text)
        self.afterEdit.setText(after_text)
        
        self.setStyleSheet(qdarkstyle.load_stylesheet())

        self.popoutOkButton.clicked.connect(self.close_window)

    def close_window(self):
        self.close()


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
