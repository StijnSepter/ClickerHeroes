import os
import time
import pyautogui


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

IMAGE_PATH = os.path.join(
    BASE_DIR,
    "../images/clock.png"
)


def boss_fight():

    try:
        return pyautogui.locateOnScreen(
            IMAGE_PATH,
            confidence=0.7,
            grayscale=True
        ) is not None

    except pyautogui.ImageNotFoundException:
        return False


def boss_confirmed(checks=3, required=2):

    detections = 0

    for _ in range(checks):

        if boss_fight():
            detections += 1

        time.sleep(0.2)

    return detections >= required