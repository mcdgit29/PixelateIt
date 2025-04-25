
# PixilateIt
A program to transform images into json data files of binary points

Original Image
![image info](./test/resources/JEdgarBuilding.jpg)

Pixilated Image
![image info](.test/resources/pixalated_image.png)

Json Results
```
{0: (1, 0), 1: (1, 1), 2: (1, 2), ...}
```

Running the Program
```shell
python PixelateIt test//resources//JEdgarBuilding.jpg --s 10 10 --r 90
```
writes results by default to results.json in directory where program is launched
