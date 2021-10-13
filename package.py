from browser import Browser
from sample import sample_entry

# create a new browser object
app = Browser(sample_entry, half_screen=True)
"""
The Browser class takes in three arguments in order: entry, URL, half_screen

Examples:
    app = Browser(URL='https://google.com')
    app = Browser(entry=sample_entry, URL='https://google.com')
    app = Browser(entry=sample_entry, URL='https://google.com', half_screen=True)
"""
app.exec_()
