from browser import Browser

app = Browser(URL='https://bing.com', screen=1)
# additional browser logic can come after this line
# Example logic to show popup with the text box's text
app.show_popup(message=app.window.textbox)
# this should always be called last
exit(app.exec_())
