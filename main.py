# import core functionalities
from sys import argv, exit
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon

# import required PyQt5 Widgtes
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView

# Browser class to create new browser application and window


class Browser(QApplication):
    def __init__(self):
        # pass in console args
        super(QApplication, self).__init__([])

        # set title and icon of browser
        self.setApplicationName('Python Browser')
        self.setWindowIcon(QIcon('./icon.png'))

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

            # display full screen
            self.showMaximized()

        def load(self, url=argv[0] if argv[1:] else 'https://google.com'):
            self.engine.setUrl(QUrl(url))


if __name__ == "__main__":
    exit(Browser().exec_())
