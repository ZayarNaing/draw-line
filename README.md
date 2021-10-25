# draw-line
## To draw a line on an image

```python draw_line.py --img <path-to-image> --save <directory where yaml file will be saved> --name <name of yaml file>```

## How to draw?
- Left Click on the mouse to mark a point anywhere on the image. When there are two marks/points on the image, the program will automatically draw line between them for you.
- You can draw any number of line you want. The program only remember the endpoints of the latest line meaning it will not store the points of the previous line.
- When you press 'q' and there is only one point of the latest line, the program will not save anything and will exit.
- When there are multiple lines on the image and if you want to clear them and start from fresh, press 'r'.
- If the result/line (must have two points) is good enough for you, press 'q' and the program will export the two endpoints of the latest line in a yaml file then the image with the latest line drawn will be display in a new window. Press 'q' and that's it.

## The structure of the yaml file
![alt text](https://github.com/ZayarNaing/draw-line/blob/main/sample_yaml.png)
