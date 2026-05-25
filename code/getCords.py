from pynput.mouse import Listener


def on_click(x, y, button, pressed):

    if pressed:
        print(f"X = {x}")
        print(f"Y = {y}")

        return False  # stop listener after first click


def find_cords():

    print("Click somewhere on the screen...")

    with Listener(on_click=on_click) as listener:
        listener.join()