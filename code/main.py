import time

from autoClicker import ClickMouse
from pynput.keyboard import Listener
from getCords import find_cords


class AutoClickerApp:
    def __init__(self):
        self.clicker = ClickMouse()


    def main(self):
        print("main")
        time.sleep(1)

        self.clicker.start()

        # keyboard listener (THIS controls SAME clicker)
        def on_press(key):
            print("Stopping clicker...")
            self.clicker.stop()
            return False

        with Listener(on_press=on_press) as listener:
            listener.join()

    def get_cords(self):
        while True:
            find_cords()


if __name__ == "__main__":
    app = AutoClickerApp()
    # app.get_cords()
    app.main()
