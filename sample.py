

def sample_entry(app):
    """This is a sample function which would be passed into
    Browser class as the first argument.

    Args:
        app (Browser): The Browser object that has been initialised
    
    Examples:
        I.  We can close the browser window and open it 
            again without exiting the browser.
        
            app.window.close() # closes the window
            app.window.show() # opens the window
        
        II. We can resize the size of the browser to
            half of the monitor's size.
    
            app.show_half_screen() # shows half screen
    
        III.We can resfresh the browser.
    
            app.refresh() # reloads the currently visited link
        
        IV. We can show a popup message
    
            app.show_popup("") # shows popup message

        V.  We can also change the current url

            app.change_url('https://example2.com')
        
        VI. To exit the browser, the exit function is Used.

            exit(1)
    """

    # uncomeent the line below to exit the browser
    # exit()
    ...
