import cv2
from PIL import Image
import numpy as np


def image2array(im: Image.Image) -> np.ndarray:
    return cv2.cvtColor(np.array(im), cv2.COLOR_RGB2BGRA)


def find_image_location(
    image: np.ndarray, template: np.ndarray
) -> tuple[float, np.ndarray]:
    alpha_channel = np.array(cv2.split(template)[3])
    result = cv2.matchTemplate(
        image, template, cv2.TM_CCOEFF_NORMED, mask=alpha_channel
    )

    _, maxVal, _, maxLoc = cv2.minMaxLoc(result, None)
    return (maxVal, maxLoc)


def load_image(path: str) -> np.ndarray:
    return cv2.imread(path, cv2.IMREAD_UNCHANGED)
