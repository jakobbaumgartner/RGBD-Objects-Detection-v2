from pynput import keyboard
import pyautogui

# define a callback function for keypress events
def on_press(key):
    try:
        # check if the key is q
        if key.char == 'q':
            # stop the listener
            return False

        # check if the key is s
        elif key.char == 's':
            # display "saved"
            print("saved")
            # move above image
            pyautogui.moveTo(2258, 360)
            # open right click menu
            pyautogui.click(button='right')
            # move mouse above save button
            pyautogui.moveTo(2358, 395)
            # save image menu
            pyautogui.click()
            # move about save button
            pyautogui.moveTo(3368, 920)
            # save image
            pyautogui.click()


        # check if the key is n
        elif key.char == 'n':
            print("next")
            pyautogui.moveTo(2700, 500)
            pyautogui.click()



    except AttributeError:
        pass

# create a listener for keypress events
with keyboard.Listener(on_press=on_press) as listener:
    # wait for the listener to stop (when q is pressed)
    listener.join()
