import pyautogui as pg

pg.PAUSE = 2
pg.FAILSAFE = True
import time

def main():
    def checkCursorPosition():
        time.sleep(2)
        print(pg.position())
        quit()


    def privateServerCheck():
        # Navigates to private server settings
        pg.click(pg.locateOnScreen('servers.png', confidence=0.95), clicks=2)
        pg.scroll(-700)
        pg.click(pg.locateOnScreen('threedots.png', confidence=0.95))
        pg.click(pg.locateOnScreen('configbutton.png', confidence=0.95))

        # Disable server joining if it is current enabled
        try:
            pg.click(pg.locateOnScreen('toggle.png', confidence=0.95))
        except pg.ImageNotFoundException:
            pass

        # Changes server name
        pg.click(pg.locateOnScreen('changenameicon.png', confidence=0.95))
        pg.click(pg.locateOnScreen('namechangebox.png', confidence=0.95))
        pg.press('backspace', presses=50)
        pg.write('This is a changed name!')
        pg.click(pg.locateOnScreen('changename.png', confidence=0.95))

        # Returns to inventory
        pg.click(pg.locateOnScreen('backarrow.png', confidence=0.95), clicks=2)


    def gameIndexLoop():
        for location in pg.locateAllOnScreen('atsymbol.png', confidence=0.90):
            pg.click(location[0], location[1] - 80)
            privateServerCheck()


    #checkCursorPosition()
    #findImages()
    privateServerCheck()
    #gameIndexLoop()

main()

