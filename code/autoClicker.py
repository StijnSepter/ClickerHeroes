import time
import threading

from pynput.mouse import Controller, Button
from nextLevel import NextLevel
from bossFight import boss_confirmed
from upgrade_units import UpgradeUnits

class ClickMouse(threading.Thread):
    def __init__(self):
        super().__init__()

        self.paused = False
        self.delay = 0.02
        self.button = Button.left
        self.mouse = Controller()

        self.running = True
        self.program_running = True

    def check_next_level(self):
        print("start threading ")
        next_level = NextLevel()
        while True:
            print("checking next level...")
            self.pause()
            next_level.next_level()
            self.resume()
            time.sleep(40)

    def boss_loop(self):
        next_level = NextLevel()
        while True:
            time.sleep(0.5)
            if boss_confirmed():
                print("Boss started")
                time.sleep(34)
                print("Boss fighting ended")
                self.pause()

                if boss_confirmed():
                    print("Boss fighting ended in defeat")
                    next_level.back_one_level()
                else:
                    print("Boss fighting ended in a win")
                    next_level.next_level()
                self.resume()
                print("Boss ended")
                time.sleep(2)

    def level_up_units(self):
        while True:
            time.sleep(30)
            if boss_confirmed():
                return
            else:
                self.pause()
                uu = UpgradeUnits()
                uu.upgrade_units()

    def stop(self):
        self.running = False
        self.program_running = False

    def pause(self):
        self.paused = True

    def resume(self):
        self.paused = False

    def run(self):
        print("running")

        threading.Thread(
            target=self.check_next_level,
            daemon=True
        ).start()

        threading.Thread(
            target=self.boss_loop,
            daemon=True
        ).start()

        threading.Thread(
            target=self.level_up_units,
            daemon=True
        ).start()

        time.sleep(1)
        while self.program_running:
            if self.running:
                if self.paused:
                    time.sleep(0.1)
                    continue
                self.mouse.click(self.button)
                time.sleep(self.delay)
