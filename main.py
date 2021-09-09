import logging
from utils.mouse_util import Mouse
from utils.cv_util import load_image, image2array, find_image_location
from utils.image_util import crop_image, take_screenshot
import time

# resources
CURSOR_TEMPLATE = load_image("resources/cursor.png")
LEFT_TEMPLATE = load_image("resources/left.png")
RIGHT_TEMPLATE = load_image("resources/right.png")
HOOK_TEMPLATE = load_image("resources/hook.png")

# --------------config-----------------
# points
indicator_region = (710, 96, 1210, 129)  # left, top, right, buttom
hook_region = (930, 137, 988, 196)
hook_acceptable_point = (21, 17)  # relative to hook_region

# other parameters
bar_length_range = (80, 160)  # pixels
match_threashhood = 0.8
sleep_time = 0.02  # seconds
# -------------end config--------------


def main():
    mouse = Mouse()
    while True:
        if not mouse.is_middle_clicked():
            time.sleep(sleep_time)
            continue

        # get image of indicator and hook
        screenshot = take_screenshot()
        indicator = image2array(crop_image(screenshot, indicator_region))
        hook = image2array(crop_image(screenshot, hook_region))

        # get the position of left arrow, right arrow, cursor and hook
        left_val, left_pos = find_image_location(indicator, LEFT_TEMPLATE)
        cursor_val, cursor_pos = find_image_location(indicator, CURSOR_TEMPLATE)
        right_val, right_pos = find_image_location(indicator, RIGHT_TEMPLATE)
        _, hook_pos = find_image_location(hook, HOOK_TEMPLATE)

        bar_length = right_pos[0] - left_pos[0]

        if (
            (left_val + cursor_val + right_val) > match_threashhood
            and (bar_length_range[0] < bar_length < bar_length_range[1])
            and hook_pos[0] == hook_acceptable_point[0]
            and hook_pos[1] == hook_acceptable_point[1]
        ):
            logging.debug(time.asctime(), left_pos, cursor_pos, right_pos)

            # if the cursor is less than 20 pixels to the right of the left arrow, then press down mouse left button
            # else, release the button
            if cursor_pos[0] - left_pos[0] < 20:
                mouse.press_left()
            else:
                mouse.release_left()

        time.sleep(sleep_time)


if __name__ == "__main__":
    main()
