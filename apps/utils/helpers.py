import math
import os

from PIL import Image


def upload_image(instance, filename):
    return os.path.join(instance._meta.model_name, '_'.join(filename.split()))


def optimize_image(image, REQUIRED_IMAGE_RATIO):
    pil_image = Image.open(image)
    width, height = pil_image.size
    if width / REQUIRED_IMAGE_RATIO[0] < height / REQUIRED_IMAGE_RATIO[1]:
        min_ratio = width / REQUIRED_IMAGE_RATIO[0]
    else:
        min_ratio = height / REQUIRED_IMAGE_RATIO[1]
    if min_ratio > 1:
        pil_image = pil_image.resize((math.ceil(width / min_ratio), math.ceil(height / min_ratio)))
        pil_image.save(image.path)
