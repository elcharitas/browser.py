# import core functionalities
from sys import argv, exit
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon

# import required PyQt5 Widgtes
from PyQt5.QtWidgets import QAction, QApplication, QLineEdit, QMainWindow, QToolBar
from PyQt5.QtWebEngineWidgets import QWebEngineView

# Browser class to create new browser application and window
class Browser(QApplication):
    def __init__(self):
        # initialize the application
        super(QApplication, self).__init__([])

        # set title and icon of browser
        self.setApplicationName('Browser')
        self.setWindowIcon(QIcon('./icon.ico'))

        # create a window
        self.window = self.Window()
        self.window.load()

    class Window(QMainWindow):
        def __init__(self):
            # create a connnection
            super(QMainWindow, self).__init__()

            # create the engine to bind
            self.engine = QWebEngineView()
            self.setCentralWidget(self.engine)

            # display full screen on any monitor
            self.showMaximized()

            # create a menubar
            menubar = QToolBar()
            self.addToolBar(menubar)
            
            # add the buttons
            Button1 = QAction('Button 1', self)
            Button2 = QAction('Button 2', self)
            menubar.addActions([Button1, Button2])

            # add the textbox
            Textbox = QLineEdit()
            menubar.addWidget(Textbox)

        def load(self, url=argv[1] if argv[1:] else 'https://google.com'):
            self.engine.setUrl(QUrl(url))

exit(Browser().exec_())
