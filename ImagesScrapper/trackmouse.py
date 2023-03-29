import pyautogui

# loop indefinitely
while True:
    # get the current mouse position
    x, y = pyautogui.position()

    # print the mouse position to the terminal
    print(f"Mouse position: x={x}, y={y}")

    # wait for a short duration before getting the next position
    pyautogui.PAUSE = 0.1
