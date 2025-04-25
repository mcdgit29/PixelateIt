import numpy as np
from PIL import Image
import subprocess


def test_pixelate_image():
    from PixelateIt.utils import pixelate_image

    p = "tests/resources/JEdgarBuilding.jpg"
    img = Image.open(p)
    img_grey = pixelate_image(img, rotation=90, threshold=160)
    assert len(np.unique(np.array(img_grey))) == 2


def test_gen_pixels():
    from PixelateIt.utils import _gen_pixels
    from PixelateIt.utils import pixelate_image

    p = "tests/resources/JEdgarBuilding.jpg"
    img = Image.open(p)
    img_grey = pixelate_image(img)
    x = list(_gen_pixels(img_grey))
    assert len(x) > 1
    assert len(x) > 1


def test_calculate_threshold():
    from PixelateIt.utils import calculate_threshold

    p = "tests/resources/JEdgarBuilding.jpg"
    img = Image.open(p)
    array = np.array(img)
    t = calculate_threshold(array)
    assert 170 > t
    assert t > 50


def test_main():
    result = subprocess.run(
        [
            "python",
            "PixelateIt",
            "tests//resources//JEdgarBuilding.jpg",
            "--s",
            "50",
            "50",
            "--r",
            "90",
            "--t",
            "160",
        ]
    )
    assert result.returncode == 0


def test_main_with_auto_calc():
    result = subprocess.run(
        [
            "python",
            "PixelateIt",
            "tests//resources//JEdgarBuilding.jpg",
            "--s",
            "10",
            "10",
            "--r",
            "90",
            "--json",
        ]
    )
    assert result.returncode == 0
