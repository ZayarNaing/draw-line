# importing the module 
import cv2 
import yaml
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("--img", type=str, help="path to image")
parser.add_argument("--save_dir", type=str, help="directory where yaml file will be saved", default="./")
parser.add_argument("--name", type=str, help="name of the yaml file", default="entry.yaml")
args = parser.parse_args()

# dictionary to store two endpoints of the line
points = {}

def save_point():
	h, w, c = image.shape
	points["startpoint"] = list(points["startpoint"])
	points["endpoint"] = list(points["endpoint"])
	points["startpoint"][0] = 0
	points["endpoint"][0] = w
	with open(os.path.join(args.save_dir, args.name), 'w') as file:
		entry = yaml.dump(points, file)

# function to display the coordinates of 
# of the points clicked on the image 
def click_event(event, x, y, flags, params): 

	# checking for left mouse clicks 
	if event == cv2.EVENT_LBUTTONDOWN: 

		# displaying the coordinates 
		# on the Shell 
		# print(x, ' ', y)

		# displaying the coordinates 
		# on the image window 
		font = cv2.FONT_HERSHEY_SIMPLEX 
		cv2.putText(image, '.', (x,y), font, 
					1, (255, 0, 0), 3) 
		cv2.imshow('image', image) 

		if "startpoint" not in points.keys() and "endpoint" not in points.keys():
			points["startpoint"] = (x, y)
		elif "startpoint" in points.keys() and "endpoint" not in points.keys():
			points["endpoint"] = (x, y)
			cv2.line(image, points["startpoint"], points["endpoint"], color=(0, 0, 0), thickness=3)
		elif "startpoint" in points.keys() and "endpoint" in points.keys():
			points.clear()
			points["startpoint"] = (x, y)
		else:
			pass 
	
if __name__=="__main__": 
	"""
	Draw a line on an image and export two endpoints of the line in a yaml file.
	"""
	if os.path.isfile(args.img):
		
	
		# reading the image
		image = cv2.imread(args.img, 1)
		clone = image.copy()

		cv2.namedWindow("image")
		# setting mouse hadler for the image 
		# and calling the click_event() function 
		cv2.setMouseCallback('image', click_event) 

		while True:
			# displaying the image 
			cv2.imshow('image', image) 
			key = cv2.waitKey(1) & 0xFF

			# press 'r' to reset the window (fresh start)
			if key == ord('r'):
				points.clear()
				image = clone.copy()

			# if key == ord('d'):
			# 	points.popitem()

			# press 'q' to quit
			if key == ord('q'):
				break

		# close the window 
		cv2.destroyAllWindows()
		if "startpoint" in points.keys() and "endpoint" in points.keys():
			print("Both endpoints are present. Exporting them to yaml file.")
			save_point()
		else:
			print("Both endpoints are not present. Quitting.")
	else:
		print("Please provide a valid image's path.")