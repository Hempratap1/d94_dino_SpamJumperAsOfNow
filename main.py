import pyautogui
import time
import keyboard
while True:

    im = pyautogui.screenshot()
    screen = im.getpixel((450, 300))
    x1 = im.getpixel((780, 277))
    x2 = im.getpixel((720, 277))
    x3 = im.getpixel((705, 277))
    x4 = im.getpixel((800, 277))

    y1 = im.getpixel((752, 253))
    y2 = im.getpixel((765, 253))
    y3 = im.getpixel((732, 253))
    y4 = im.getpixel((708, 189))

    if screen[0] == 255:
        if x1[0] != 255 or x2[0] != 255 or x3[0] != 255 or x4[0] != 255 or y1[0] != 255 or y2[0] != 255 or y3[0] != 255 or y4[0] != 255:
            pyautogui.press('space')
            time.sleep(0.6)

    else:
        if x1[0] != 0 or x2[0] != 0 or x3[0] != 0 or x4[0] != 0 or y1[0] != 0 or y2[0] != 0 or y3[0] != 0 or y4[0] != 0:
            pyautogui.press('space')
            time.sleep(0.7)

    if keyboard.is_pressed('s'):
        break
    #  trial code i tried making it work but it kind of stops wrking after first or second jump hehe :D
    # im = pyautogui.screenshot()
    #     if pyautogui.pixelMatchesColor(820, 300, target_colour, tolerance=15):
    #         pyautogui.press('space')
    #         time.sleep(0.3)
