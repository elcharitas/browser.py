from browser import Browser
from threading import Thread

# create a thread for the app so we can run the while oop
app = Browser(screen=2)
Thread(target=app.exec_).start()

"""This loop will keep running until exited with Ctrl-C or any other terminating signal
To quit the browser, simply use app.quit()
"""
while True:
    try:
        command = input("Please enter command: ")
        if command == "quit":
            break
        elif command:
            def a(): return exec(command)
        a()
    except Exception as Except:
        print("error live session -- ", Except)
