from PIL import Image, ImageFilter
import numpy as np
from itertools import product
from sklearn.cluster import KMeans


def pix_binary(x: int, top=100) -> int:
    """
    Pixel Binary calculation
    :param x: Integer
    :param top: Integer between 0-252
    :return: int either 0 or 252
    """
    if x >= top:
        return 252
    else:
        return 0


def calculate_threshold(array: np.array) -> int:
    """
    Calculates the Midpoint between two clusters detected from
    the flattened array

    :param array: np array
    :return: int
    """
    x = array.reshape(-1,1)
    model = KMeans(n_clusters=2, random_state=0).fit(x)
    y = model.labels_
    center_0 = np.mean(x[y==0, :])
    center_1 = np.mean(x[y==1, :])
    min_center = np.min([center_0, center_1])
    mid = np.absolute(center_0 - center_1)
    t = int(min_center + mid/2)
    print(F'calculated threshold: {t}')
    return t


def pixelate_image(img: Image, size: (int, int) = (100, 100),
                   rotation: int = 0, threshold: int = None):
    """
    _gen_pixels Resizes, rotations and binarizes images,
    and yields tuples of pixels

    :param img: PIL image
    :param size: tuple (int, int) width, height
    :param rotation: int, 0-360 amount to rotate image
    :param threshold:int 0-255, setting low returns more pixels,
    higher returns fewer
    :return: PIL image, binary of size and rotation specified
    """
    if threshold is None:
        threshold = calculate_threshold(np.array(img))
    img_grey = img.convert('L')\
        .rotate(rotation)\
        .filter(ImageFilter.MaxFilter)\
        .resize(size)\
        .filter(ImageFilter.EDGE_ENHANCE_MORE)\
        .point(lambda p: pix_binary(p, threshold))
    return img_grey


def _gen_pixels(img: Image):
    """
    _gen_pixels Resizes, rotations and binarizes images,
    and yields tuples of pixels

    :param img: PIL image
    :return: generator yield tuples of i,j pixel locations
    """
    array = np.array(img)

    # calculates threshold for binarization
    threshold = (np.max(array) - np.min(array))/2 + np.min(array)
    for i, j in product(range(array.shape[0]), range(array.shape[1])):
        if array[i, j] > threshold:
            yield i, j
