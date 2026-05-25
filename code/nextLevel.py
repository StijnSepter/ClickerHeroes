import pyautogui


class NextLevel:
    def __init__(self):
        self.x = 1360
        self.y = 150
        self.back_x = 1200
        self.back_y = 150
        self.attack_x = 1281
        self.attack_y = 581

    def next_level(self):
        print("Next Level")
        pyautogui.click(self.x, self.y)
        self.back_to_attacking()

    def back_one_level(self):
        print("Back One Level")
        pyautogui.click(self.back_x, self.back_y)
        self.back_to_attacking()

    def back_to_attacking(self):
        pyautogui.moveTo(self.attack_x, self.attack_y)

