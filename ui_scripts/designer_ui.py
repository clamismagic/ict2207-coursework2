# import all for now
from email import message
from http.client import OK
from tkinter import E, Widget, messagebox
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PyQt5.uic import loadUi
from PyQt5.QtGui import *
from obfuscator_scripts import controller
from ui_scripts import obfuscator
import os
import sys
import qdarkstyle
import magic

script_dir = os.path.dirname(__file__)
mymodule_dir = os.path.join(script_dir, '..', 'obfuscator_scripts')
sys.path.append(mymodule_dir)


def exit_program():
    quit()


class MainWindow(QMainWindow, obfuscator.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.setStyleSheet(qdarkstyle.load_stylesheet())

        self.actionExit.triggered.connect(exit_program)
        self.apkbrowseButton.clicked.connect(self.apk_browse)
        self.obfuscateButton.clicked.connect(self.obfuscate)
        self.keystoreBrowseButton.clicked.connect(self.keystore_browse)

    def apk_browse(self):
        file_path = QFileDialog.getOpenFileName(self, 'Open APK File', "", "Android Package File (*.apk)")
        # print(file_path[0])
        self.apkpathEdit.setText(file_path[0])

    def keystore_browse(self):
        key_path = QFileDialog.getOpenFileName(self, 'Open JKS File', "", "JKS File (*.jks)")
        # print(key_path[0])
        self.keystorePathEdit.setText(key_path[0])

    def obfuscate(self):
        print(magic.from_file(self.apkpathEdit.text()))
        if self.apkpathEdit.text() != '' and "Zip archive data" in magic.from_file(self.apkpathEdit.text()):
            try:
                controller.Controller(self.apkpathEdit.text())
                for x in range(5):
                    tab_window = QWidget(self)
                    before_text = QTextEdit(self)
                    after_text = QTextEdit(self)
                    tab_layout = QHBoxLayout()
                    tab_layout.addWidget(before_text)
                    tab_layout.addWidget(after_text)

                    self.tabWidget.addTab(tab_window, str(x))
            except Exception as e:
                print("Error: {0}".format(e))
                raise

        else:
            message_box = QMessageBox()
            message_box.setStyleSheet(qdarkstyle.load_stylesheet())
            message_box.setWindowTitle("Error")
            message_box.setText("Incorrect File Provided!")
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
