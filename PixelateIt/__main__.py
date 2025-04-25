import json
from PIL import Image
from PixelateIt.utils import _gen_pixels
from PixelateIt.utils import pixelate_image
import argparse
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(add_help=True,
                                     description="Pixelate Images, "
                                                 "returns json "
                                                 "output of pixel locations")
    parser.add_argument('i', nargs='?',  type=Path,
                        help="input image file path")
    parser.add_argument('--o', required=False, type=str,
                        help="path to write json output")
    parser.add_argument('--s', default=(50, 50), type=int, nargs=2,
                        help="int: width, height to resize image")
    parser.add_argument('--r', default=0, type=int,
                        help="int degree of rotation for image")
    parser.add_argument('--t', type=int,
                        help='int 0-255 threshold for image binerization')
    parser.add_argument('--json', help='returns json of points',  action='store_true', default=False)
    args = parser.parse_args()

    # input file
    input_file = Path(args.i)

    if input_file.is_file() is False:
        raise FileExistsError(f"could not find: {input_file}")

    # size
    s = args.s

    # threshold
    t = args.t

    # rotation
    r = args.r

    # whether to write json or image
    write_json = args.json

    if args.o:
        output_path = Path(args.o)
    else:
        if write_json:
            output_path = str(Path(input_file))
            output_path = Path(output_path[:-3] + 'json')
        else:
            output_path = str(Path(input_file))
            img_type = output_path[-4:]
            output_path = Path(output_path[:-4] + '__pixelated__' + img_type)

    with Image.open(input_file) as img:
        img_bi = pixelate_image(img, size=s, rotation=r, threshold=t)

    points = list(_gen_pixels(img_bi))
    d = dict()
    for i, val in enumerate(points):
        d[i] = val
    if write_json:
        with open(output_path, 'w') as f:
            json.dump(d, f)
    else:
        img_bi.save(output_path)

    img_bi.show()
    print(d)
    print(F'Image Size: {s} Number of Points: {len(points)}')
    print(F"output written to: {Path(output_path).absolute()}")


if __name__ == "__main__":
    main()