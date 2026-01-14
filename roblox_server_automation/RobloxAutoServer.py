# Roblox Local Private Server Disable and Rename Automation Tool
# Last Updated: 01/14/2025
#
# INSTRUCTIONS:
# 1. Download the reference images folder.
# 2. Set the variables: pages_in_inventory, server_name, and file_path.
# 3. Open Roblox → Inventory → Private Servers.
# 4. Scroll to the top of the Private Servers page.
# 5. Move the Roblox window to occupy half of your monitor.
# 6. Run the program.

import pyautogui as pg
import time

# Move cursor to top left of screen to abort program
pg.FAILSAFE = True


def main():
    # Customizable variables
    pages_in_inventory = 9 # Number of pages in private server inventory
    server_name = 'N' # Name all servers will be changed to
    file_path = 'ReferenceImages\\' # Complete file path to folder with reference images


    # Helper functions
    # Locates image
    def locate(file, confidence=0.95):
        return pg.locateOnScreen(f"{file_path}{file}.png", confidence=confidence)

    # Clicks on image
    def click(file, confidence=0.95, clicks=1, interval=0.0):
        pg.click(locate(file, confidence), clicks=clicks, interval=interval)

    # Checks if image is visible on screen
    def image_exists(file, confidence=0.95):
        try:
            locate(file)
            return True
        except pg.ImageNotFoundException:
            return False


    # Loops through visible private servers
    # Calls privateServerCheck for each server
    # Uses hotkey to open and switch to new tab with game
    def gameIndexLoop():
        # Uses @ symbol in username to find locations of game icons
        for location in pg.locateAllOnScreen(file_path + 'at-symbol-R.png', confidence=0.93):
            pg.moveTo(location[0], location[1] - 70)
            pg.keyDown('ctrl')
            pg.keyDown('shift')
            pg.click()
            pg.keyUp('ctrl')
            pg.keyUp('shift')
            time.sleep(2)
            privateServerCheck()


    # Navigates to private server settings
    # Disables server and changes name
    def privateServerCheck():
        pg.scroll(-400)
        time.sleep(0.5)

        # Returns to gameIndexLoop if game or server no longer supported
        if image_exists('not-found-R') or image_exists('no-support-R'):
                pg.hotkey('ctrl', 'w')
                time.sleep(0.5)
                return

        # Navigates to private server settings
        click('three-dots-B')
        click('config-B')
        time.sleep(2)

        # Disables server joining if it is current enabled
        try:
            click('server-toggle-B')
        except pg.ImageNotFoundException:
            pass

        # Changes server name to user input
        click('change-name-B')
        click('name-box-B')
        pg.press('backspace', presses=50)
        pg.write(server_name)
        click('name-confirm-B')

        # Closes tab to return to inventory
        pg.hotkey('ctrl', 'w')
        time.sleep(0.5)


    # Scrolls down until "Page" to ensure half the servers are showing
    # Saves as scroll amount to use repeatedly
    scroll_amt = 0
    click('my-servers-R')
    while True:
        if image_exists('page-text-R'):
            break
        pg.scroll(-50)
        scroll_amt -= 50


    # Loops through top and bottom of pages in inventory
    for page_number in range (1, pages_in_inventory):
        pg.hotkey('ctrl', 'home')
        time.sleep(0.5)
        gameIndexLoop()
        pg.scroll(scroll_amt)
        gameIndexLoop()
        click('next-page-B')
        time.sleep(0.5)


if __name__ == "__main__":
    main()

