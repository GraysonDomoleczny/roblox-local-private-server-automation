# Roblox Local Private Server Disable and Rename Automation Tool
# Last Updated: 01/11/2025

import pyautogui as pg
import time

# Move cursor to top left of screen to abort program
pg.FAILSAFE = True


def main():
    # Customizable variables
    load_delay_in_seconds = 2 # Higher delay for slower devices
    pages_in_inventory = 9 # Number of pages in private server inventory
    server_name = 'N' # Name all servers will be changed to
    file_path = 'ReferenceImages\\' # Complete file path to folder with reference images


    # Loops through visible private servers
    # Calls privateServerCheck for each server
    def gameIndexLoop():
        # Clicks on game icon based on @ symbol in username
        for location in pg.locateAllOnScreen(str(file_path + 'atsymbolreference.png'), confidence=0.90):
            pg.click(location[0], location[1] - 80)
            time.sleep(load_delay_in_seconds)
            privateServerCheck()


    # Navigates to private server settings
    # Disables server and changes name
    def privateServerCheck():
        # Navigates to private server settings
        pg.click(pg.locateOnScreen(str(file_path + 'serverstab.png'), confidence=0.95), clicks=2)
        while True:
            try:
                pg.locateOnScreen(str(file_path + 'threedotsbutton.png'), confidence=0.95)
                break
            except pg.ImageNotFoundException:
                pg.scroll(-200)
        pg.click(pg.locateOnScreen(str(file_path + 'threedotsbutton.png'), confidence=0.95))
        pg.click(pg.locateOnScreen(str(file_path + 'configbutton.png'), confidence=0.95))
        time.sleep(load_delay_in_seconds)

        # Disable server joining if it is current enabled
        try:
            pg.click(pg.locateOnScreen(str(file_path + 'servertoggle.png'), confidence=0.95))
        except pg.ImageNotFoundException: pass

        # Changes server name to user input
        pg.click(pg.locateOnScreen(str(file_path + 'changenameicon.png'), confidence=0.95))
        pg.click(pg.locateOnScreen(str(file_path + 'namechangebox.png'), confidence=0.95))
        pg.press('backspace', presses=50)
        pg.write(server_name)
        pg.click(pg.locateOnScreen(str(file_path + 'changenamebutton.png'), confidence=0.95))

        # Returns to inventory
        pg.click(pg.locateOnScreen(str(file_path + 'chromebackarrow.png'), confidence=0.95), clicks=2)
        time.sleep(load_delay_in_seconds)


    # Loops through number of pages in inventory
    # scrolls down as needed and uses visual elements to determine when to stop
    for page_number in range (1, pages_in_inventory):
        #gameIndexLoop()

        # Scrolls down until "Page" to ensure half the servers are showing
        pg.click(pg.locateOnScreen(str(file_path + 'myinventoryreference.png'), confidence=0.95))
        while True:
            try:
                pg.locateOnScreen(str(file_path + 'inventorypagereference.png'), confidence=0.9)
                break
            except pg.ImageNotFoundException:
                pg.scroll(-50)

        gameIndexLoop()

        # Moves to top of next page
        pg.click(pg.locateOnScreen(str(file_path + 'nextpagearrow.png'), confidence=0.9))
        time.sleep(load_delay_in_seconds)
        pg.hotkey('ctrl', 'home')
        time.sleep(1)


if __name__ == "__main__":
    main()

