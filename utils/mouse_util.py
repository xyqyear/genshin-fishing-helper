import mouse
import logging


class Mouse:
    def __init__(self) -> None:
        self._left_down = False
        self._middle_clicked = True

        def _callback():
            # x = x xor True means toggle
            self._middle_clicked ^= True
            logging.info(f"Program {'disabled' if self._middle_clicked else 'enabled'}")

        mouse.on_middle_click(_callback)

    def press_left(self):
        """
        press down mouse left button if not
        """
        if not self._left_down:
            mouse.press()
            self._left_down ^= True

    def release_left(self):
        """
        release mouse left button if pressed
        """
        if self._left_down:
            mouse.release()
            self._left_down ^= True

    def is_middle_clicked(self):
        return self._middle_clicked
