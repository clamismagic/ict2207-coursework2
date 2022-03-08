# import all for now
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PyQt5.uic import loadUi
from PyQt5.QtGui import *

from obfuscator import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.apkbrowseButton.clicked.connect(self.apkBrowse)
        self.keystoreBrowseButton.clicked.connect(self.keystoreBrowse)

    def apkBrowse(self):
        filePath = QFileDialog.getOpenFileName(self, 'Open APK File', "", "Android Package File (*.apk)")
        print (filePath[0])
        self.apkpathEdit.setText(filePath[0])

    def keystoreBrowse(self):
        keyPath = QFileDialog.getOpenFileName(self, 'Open JKS File', "", "JKS File (*.jks)")
        print (keyPath[0])
        self.keystorePathEdit.setText(keyPath[0])


def main():

    # You need one (and only one) QApplication instance per application.
    # Pass in sys.argv to allow command line arguments for your app.
    # If you know you won't use command line arguments QApplication([]) works too.
    app = QApplication([])

    # Create a Qt widget, which will be our window.
    window = MainWindow()
    window.show()  # IMPORTANT!!!!! Windows are hidden by default.

    # Start the event loop.
    app.exec_()


if __name__ == "__main__":
    main()