
# PixilateIt
A program to transform images into json data files of binary points.
This package's intended use is to take a hand drawn image on a white background and extract the pixels of the drawing into an arbitrary re-sized image

## Project status
This is a demo project, has no warranty, is not supported and generally only exists because the author though it was sort of interesting.


Original Image
<img src="tests/resources/JEdgarBuilding.jpg" alt="Alt Text" width="150" height="100">


Pixilated Image
<img src="tests/resources/JEdgarBuilding__pixelated__.jpg" alt="Alt Text" width="100" height="100">

### Optional Json Results
Using the --json flag, a file is created of the pixals used to created the pixaleted image. 
Keys are the index of each point, values are tuple with the row, column for each non-white pixel
```
{0: (1, 0), 1: (1, 1), 2: (1, 2), ...}
```

Installation (using python 3.11), recommended installation into a virtual environment.
Requires Python 3.11 (may or may not work in other environments)
+ Clone the repository
  ```shell
  git clone git@github.com:mcdgit29/PixelateIt.git
  ```
+ cd into the PixilateIt directory that contains the poetry.toml file
+ install with pip
 ```shell
  pip install .
```

## Usage in the command line
this example shows resizing the image to 10 x 10 and rotating it 90 degrees and uses the automatic detection of the threshold for bininarization. 
```shell
python PixelateIt tests//resources//JEdgarBuilding.jpg --s 10 10 --r 90
```

### Options

writes results by default to results.json in directory where program is launched
+ Use --json flag to write json results (key is the index of points, value is a tuple with the row and column of the point)
+ -s int, int defines the resizing of the image.
+ -r int, defines degree of rotation of the image.
+ -t defines the threshold to binerize, automatically defected if left blank. between 0-254, smaller number means results in more pixels


### Testing
use tox in shell
