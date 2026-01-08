import pyautogui
pyautogui.PAUSE = 2
pyautogui.FAILSAFE = True
import time

def main():
    #test

    def checkCursorPosition():
        time.sleep(2)
        print(pyautogui.position())
        quit()

    def findImages():
        # should be roughly 550, 330
        print(pyautogui.locateCenterOnScreen('changename.png', confidence=0.95))

    def privateServerCheck():
        #navigate to private server settings
        pyautogui.click(280, 394)
        pyautogui.scroll(-500)
        pyautogui.click(883, 732)
        pyautogui.click(883, 775)

        #change name
        #position of edit button on name changes with length of name
        pyautogui.click(pyautogui.locateCenterOnScreen('changename.png', confidence=0.95))
        pyautogui.click(657, 582)
        pyautogui.press('backspace', presses=50)
        pyautogui.write('This is a changed name!')
        pyautogui.click(418, 641)

        #return to inventory
        pyautogui.click(21, 63)
        pyautogui.click(21, 63)


    def gameIndexLoop():
        # monitor size 1920 x 1080
        # 138x 245y between roblox games on half screen monitor
        # starting 280x 394y
        vertical_index = 0
        y_offset = 394
        while vertical_index < 3:
            horizontal_index = 0
            x_offset = 280
            while horizontal_index < 5:
                print(pyautogui.position())
                pyautogui.moveTo(x_offset, y_offset)
                x_offset += 138
                horizontal_index += 1
            y_offset += 245
            vertical_index += 1

    #checkCursorPosition()
    #findImages()
    privateServerCheck()

main()

