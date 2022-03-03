from gc import get_threshold
import sys

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


        #Set layout
        mainLayout = QVBoxLayout()
        tabLayout = QHBoxLayout()
        filesLayout = QHBoxLayout()
        textLayout = QHBoxLayout()
        keysLayout = QHBoxLayout()


        #File layout
        filesLayout.addWidget(Color('red'))
        filesLayout.addWidget(Color('yellow'))
        filesLayout.addWidget(Color('purple'))
        filesLayout.addWidget(Color('black'))
        mainLayout.addLayout(filesLayout)

        #Tab layout
        tabLayout.addWidget(Color("gold"))
        mainLayout.addLayout(tabLayout)
        
        #Textbox output layout
        textLayout.addWidget(Color('red'))
        textLayout.addWidget(Color('purple'))
        mainLayout.addLayout(textLayout)

        #Key layouts
        keysLayout.addWidget(Color('red'))
        keysLayout.addWidget(Color('purple'))
        keysLayout.addWidget(Color('yellow'))
        keysLayout.addWidget(Color('purple'))
        keysLayout.addWidget(Color('black'))
        mainLayout.addLayout(keysLayout)



        widget = QWidget()
        widget.setLayout(mainLayout)
        self.setCentralWidget(widget)


        


        #Size of Windows
        self.setMinimumSize(QSize(1200, 800))



        #Menu

        exitMenuButton = QAction("Exit", self)
        exitMenuButton.setStatusTip("Exit menu button")
        exitMenuButton.triggered.connect(self.onExitMenuButtonClick)

        menu = self.menuBar()

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