import pyautogui as pg
import time

# Move cursor to top left of screen to abort program
pg.FAILSAFE = True

def main():
    load_delay_in_seconds = 2 # Higher delay for slower devices
    pages_in_inventory = 9 # Number of pages in private server inventory
    server_name = 'N' # Name all servers will be changed to


    #Test Function
    #checkCursorPosition()
    def checkCursorPosition():
        time.sleep(2)
        print(pg.position())
        quit()


    # Loops through visible private servers
    # Calls privateServerCheck for each server
    def gameIndexLoop():
        # Clicks on game icon based on @ symbol in username
        for location in pg.locateAllOnScreen('atsymbol.png', confidence=0.90):
            pg.click(location[0], location[1] - 80)
            time.sleep(load_delay_in_seconds)
            privateServerCheck()


    # Navigates to private server settings
    # Disables server and changes name
    def privateServerCheck():
        # Navigates to private server settings
        pg.click(pg.locateOnScreen('servers.png', confidence=0.95), clicks=2)
        while True:
            try:
                pg.locateOnScreen('threedots.png', confidence=0.95)
                break
            except pg.ImageNotFoundException:
                pg.scroll(-200)
        pg.click(pg.locateOnScreen('threedots.png', confidence=0.95))
        pg.click(pg.locateOnScreen('configbutton.png', confidence=0.95))
        time.sleep(load_delay_in_seconds)

        # Disable server joining if it is current enabled
        try:
            pg.click(pg.locateOnScreen('toggle.png', confidence=0.95))
        except pg.ImageNotFoundException: pass

        # Changes server name to user input
        pg.click(pg.locateOnScreen('changenameicon.png', confidence=0.95))
        pg.click(pg.locateOnScreen('namechangebox.png', confidence=0.95))
        pg.press('backspace', presses=50)
        pg.write(server_name)
        pg.click(pg.locateOnScreen('changename.png', confidence=0.95))

        # Returns to inventory
        pg.click(pg.locateOnScreen('backarrow.png', confidence=0.95), clicks=2)
        time.sleep(load_delay_in_seconds)


    # Loops through all 30 servers in page
    # Moves to next page
    def inventoryLoop():
        page_number = 1
        while page_number < pages_in_inventory:
            gameIndexLoop()

            while True:
                try:
                    pg.locateOnScreen('inventorypage.png', confidence=0.95)
                    break
                except pg.ImageNotFoundException:
                    pg.scroll(-50)

            gameIndexLoop()

            pg.click(pg.locateOnScreen('inventoryarrow.png', confidence=0.95))
            page_number += 1
            time.sleep(load_delay_in_seconds)
            pg.hotkey('ctrl', 'home')
            time.sleep(1)


    inventoryLoop()

main()

