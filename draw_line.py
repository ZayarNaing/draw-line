import cv2 
import argparse
import os
import yaml


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--img", type=str, help="path to image")
    parser.add_argument("--save_dir", type=str, help="directory where yaml file will be saved", default="./")
    parser.add_argument("--name", type=str, help="name of the yaml file", default="entry.yaml")
    args = parser.parse_args()
    return args

drawing = False
startpoint = None
endpoint = None 
second_click = False

def line_drawing(event, x, y, flags, params):
    global startpoint, drawing, endpoint, second_click
    if event == cv2.EVENT_LBUTTONDOWN:
        if drawing == False:
            drawing = True
            second_click = False
            startpoint = (x, y)
        elif drawing == True:
            drawing = False
            second_click = True
            endpoint = (x, y)

    if event == cv2.EVENT_MOUSEMOVE:
        endpoint = (x, y)

def export_points(s, e, save_dir, name):
    """
    Export two points of entry line to yaml file

    Parameters
    ----------
    s : tuple
        (x, y) coordinates of start point of entry line
    e : tuple
        (x, y) coordinates of end point of entry line
    """
    points = {
        "startpoint" : list(s),
        "endpoint" : list(e)
    }
    with open(os.path.join(save_dir, name), 'w') as file:
        entry = yaml.dump(points, file)

def main():
    """
    Main function
    """
    global drawing, startpoint, endpoint, second_click
    args = parse_args()
    # reading the image
    image = cv2.imread(args.img, 1)
    clone = image.copy()
    cv2.namedWindow("IMAGE")
    cv2.setMouseCallback("IMAGE", line_drawing)

    while True:
        if drawing:
            image = clone.copy()
            cv2.line(image, startpoint, endpoint, (0,0,255), thickness=3)

        cv2.imshow("IMAGE", image)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('c') or key == ord('r'):
            # press 'c' or 'r' to reset the window
            startpoint = None
            endpoint = None
            drawing = False
            image = clone.copy()

        if key == 13 or key == ord('q'):
            # press 'q' or 'ENTER' to quit
            if not(drawing == False and second_click == True):
                print("Either one of two points missing. Exiting the program without saving the points.")
            else:
                print("Both points of entry line present.\n[{}, {}]\nSaving points to {}".format(startpoint, endpoint,args.save_dir + args.name))
                export_points(startpoint, endpoint, args.save_dir, args.name)
            break

    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
