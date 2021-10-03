# import core functionalities
from sys import argv, exit
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon

# import required PyQt5 Widgtes
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QLineEdit,
    QPushButton,
    QWidget,
    QVBoxLayout,
    QHBoxLayout
)
from PyQt5.QtWebEngineWidgets import QWebEngineView

# Browser class to create new browser application and window
class Browser(QApplication):

    # known screens and name
    _screens = ['Screen 1']

    def __init__(self, URL=argv[1] if argv[1:] else 'https://google.com', screen=1):
        # initialize the application
        super(QApplication, self).__init__([])

        # set title and icon of browser
        self.setApplicationName('Browser')
        self.setWindowIcon(QIcon(':icon.ico'))

        # create a window and load it
        self.window = self.Window()
        self.window.load(URL)

        self.screen = screen if self.has_screen(screen) else 1
    
    @property
    def screens(self):
        return enumerate([None] + self._screens)
    
    def has_screen(self, screen):
        return hasattr(self.screens, screen)

    class Window(QMainWindow):
        def __init__(self):
            # create a connnection
            super(QMainWindow, self).__init__()

            # create a container and its layout
            self.container = QWidget()
            self.layout = QVBoxLayout()
            self.container.setLayout(self.layout)
            self.setCentralWidget(self.container)

            # create the engine to bind
            self.engine = QWebEngineView()
            self.layout.addWidget(self.engine)

            # create a menubar layout
            menubar = QHBoxLayout()
            self.layout.addLayout(menubar)
            
            # create refresh button and add to layout
            ButtonH = QPushButton('Refresh', self)
            ButtonH.pressed.connect(self.load)
            menubar.addWidget(ButtonH)

            # create extra button
            Button2 = QPushButton('Button 2', self)
            menubar.addWidget(Button2)

            # add the textbox
            Textbox = QLineEdit()
            menubar.addWidget(Textbox)

            # display full screen on any monitor
            self.showMaximized()

        def load(self, url: str):
            self.engine.setUrl(QUrl(url))

exit(Browser().exec_())
