# import core functionalities
from sys import argv, exit
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon
from screeninfo import get_monitors

# import required PyQt5 Widgtes
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QLineEdit,
    QMessageBox,
    QPushButton,
    QWidget,
    QVBoxLayout,
    QHBoxLayout
)
from PyQt5.QtWebEngineWidgets import QWebEngineView

# Browser class to create new browser application and window


class Browser(QApplication):
    
    # list of autodetected screens
    screens = get_monitors()

    def __init__(self, URL=argv[1] if argv[1:] else 'https://google.com', screen=argv[2] if len(argv) > 1 else 1):
        # initialize the application
        super(QApplication, self).__init__([])

        # set title and icon of browser
        self.setApplicationName('Browser')
        self.setWindowIcon(QIcon(':icon.ico'))

        # resolve the screen before creating the wndow
        self.screen = screen if self.has_screen(screen) else self.show_popup(message='Using default Screen!') or 1

        # create a window and load it
        self.window = self.Window(self.screen)
        self.change_url(URL)
    
    def has_screen(self, screen):
        """Used internally to check if a screen is supported or existing

        Args:
            screen (int): The ID of the screen

        Returns:
            bool: true if the screen exists
        """        
        return screen <= len(self.screens) and screen > 0
    
    def change_url(self, url: str):
        """Changes the URL the engine is to load

        Args:
            url (str): new url to load
        
        Example:
            app = Browser('https://example.com')
            app.change_url('https://example2.com')
        """        
        self.window.engine.setUrl(QUrl(url))
    
    def hide_menubar(self, disabled=True):
        """Hides/Shows the menu bar when disabled is True/False

        Args:
            disabled (bool, optional): Whether or not to hide the menubar. Defaults to True.
        
        Example:
            app = Browser('https://example.com')
            app.hide_menubar()
        """        
        if disabled is not False:
            self.window.menubar.show()
        else:
            self.window.menubar.hide()
    
    def show_popup(self, message='It\'s working!'):
        """Displays a popup message.

        Args:
            message (str, optional): The message to display. Defaults to 'It\'s working!'.
        
        Example:
            app.show_popup(message='Some Message')
        """
        messageBox = QMessageBox()
        messageBox.setText(message)
        messageBox.exec_()

    class Window(QMainWindow):
        def __init__(self, screen):
            # create a connnection
            super(QMainWindow, self).__init__()

            self.browser = Browser.instance()

            # create a container and its layout
            self.container = QWidget()
            self.layout = QVBoxLayout()
            self.container.setLayout(self.layout)
            self.setCentralWidget(self.container)

            # create the engine to bind
            self.engine = QWebEngineView()
            self.layout.addWidget(self.engine)

            # create the menubar
            menubar = QHBoxLayout()

            # create refresh button and add to layout
            ButtonH = QPushButton('Refresh', self)
            ButtonH.pressed.connect(self.refresh_browser)
            menubar.addWidget(ButtonH)

            # create extra button
            Button2 = QPushButton('Button 2', self)
            menubar.addWidget(Button2)

            # add the textbox
            self.TextBox = QLineEdit()
            menubar.addWidget(self.TextBox)

            # add the widget to layout
            self.menubar = QWidget()
            self.menubar.setLayout(menubar)
            self.menubar.setMaximumHeight(40)
            self.layout.addWidget(self.menubar)
            
            # display the appropiate screen
            self.resolve_screen(screen)
        
        def refresh_browser(self):
            """Refreshes the browser by revisiting the current link
            """
            self.engine.setUrl(QUrl(self.engine.url()))
        
        def resolve_screen(self, screen):
            """Resolves the screen/monitor

            Args:
                screen (int): The appropiate screen number
            """            
            if self.browser.has_screen(screen):
                if screen == 1:
                    # display full screen on any monitor
                    self.showFullScreen()
                else:
                    self.setFixedWidth(self.browser.screens[screen].width)
                    self.setFixedHeight(self.browser.screens[screen].height)
            else:
                self.browser.show_popup(message='Unsupported Screen!')
        
        @property
        def textbox(self):
            """Get the text within the textbox as a variable
            
            Example:
                app = Browser('https://example.com')
                print(app.window.textbox)
            """
            return self.TextBox.text()
