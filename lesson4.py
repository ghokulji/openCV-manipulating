from __future__ import print_function
import argparse
import cv2

obj = argparse.ArgumentParser()
obj.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(obj.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("     ", image)

(b,g,r) = image[0, 0]
print("Pixel at (0,0) -R: {}, G: {}, B: {}".format(r,g,b))

image[0, 0] = (0,0,255)
(b,g,r) = image[0, 0]
print("Pixel at [0,0] -R: {}, G: {}, B: {}".format(r,g,b))

corner = image[0:100, 0:100]
cv2.imshow("corner", corner)

image[0:100, 0:100] = (255, 0, 0)
cv2.imshow("Updated", image)
cv2.waitKey(0)
