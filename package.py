from browser import Browser

# create a new browser
app = Browser().exec_()
# head on to browser.py and edit Browser::waiter
# or simply create a new class to extend it
# and define a new waiter method
"""Example of extending Browser class
class NewBrowser(Browser):
    def waiter(self, closed=False):
        while closed == True:
            print('It works')
"""
