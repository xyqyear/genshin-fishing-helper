from PIL import Image, ImageGrab


def take_screenshot() -> Image.Image:
    return ImageGrab.grab()


def crop_image(im: Image.Image, region: tuple[int, int, int, int]) -> Image.Image:
    return im.crop(region)
