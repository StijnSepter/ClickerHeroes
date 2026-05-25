import pyautogui


class UpgradeUnits:
    def __init__(self):
        self.x_pos = 157
        self.y_pos = 545
        self.x_scroll_top = 783
        self.y_scroll_top = 472
        self.x_scroll_bottom = 783
        self.y_scroll_bottom = 1036
        self.attack_x = 1281
        self.attack_y = 581

    def upgrade_units(self):
        for _ in range(10):
            pyautogui.click(self.x_pos, self.y_pos)
        self.back_to_attacking()

    def scroll_up(self):
        pyautogui.click(self.x_scroll_top, self.y_scroll_top)
        self.back_to_attacking()

    def scroll_down(self):
        pyautogui.click(self.x_scroll_bottom, self.y_scroll_bottom)
        self.back_to_attacking()

    def back_to_attacking(self):
        pyautogui.moveTo(self.attack_x, self.attack_y)
