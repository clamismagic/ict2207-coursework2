from gc import get_threshold
import sys
from turtle import color

# import all for now
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

#Class for Colors
class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
     
        super().__init__()

        #Title
        self.setWindowTitle("APK Obfuscator")

        #Labels and Buttons
        titleLabel = QLabel("APK OBFUSCATOR")
        titleFont = QFont()
        titleFont.setBold(True)
        titleLabel.setFont(titleFont)

    
        apkpathLabel = QLabel("APK Path: ")
        apkpathEdit = QLineEdit()
        apkpathButton = QPushButton()

        projectnameLabel = QLabel("Project Name: ")
        projectnameEdit = QLineEdit()

        obfuscateButton = QPushButton()
       
        
        #Set layout
        mainLayout = QGridLayout()
        # (0, 0), (0, 1), (0, 2), (0, 3),
        # (1, 0), (1, 1), (1, 2), (1, 3),
        # (2, 0), (2, 1), (2, 2), (2, 3),
        # (3, 0), (3, 1), (3, 2), (3, 3 ),
        # (4, 0), (4, 1), (4, 2), (4, 3)
     
        mainLayout.addWidget(titleLabel, 0, 0)

        mainLayout.addWidget(apkpathLabel, 1, 0)
        mainLayout.addWidget(apkpathEdit, 1, 1)
        mainLayout.addWidget(apkpathButton, 1 , 3)

        mainLayout.addWidget(projectnameLabel, 2, 0)
        mainLayout.addWidget(projectnameEdit, 2, 1)

        mainLayout.addWidget(obfuscateButton, 1, 4, 2, 2)


        widget = QWidget()
        widget.setLayout(mainLayout)
        self.setCentralWidget(widget)


        


        #Size of Windows
        self.setMinimumSize(QSize(1200, 800))

        #Set Background Color
        
        # self.setStyleSheet("background-color: #262626;")

        #Menu
        exitMenuButton = QAction("Exit", self)
        exitMenuButton.setStatusTip("Exit menu button")
        exitMenuButton.triggered.connect(self.onExitMenuButtonClick)
        menu = self.menuBar()
        menu.setStyleSheet("background-color: white;")
        file_menu = menu.addMenu("&File")
        file_menu.addAction(exitMenuButton)
   

    def onExitMenuButtonClick(self):
        exit()
        
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