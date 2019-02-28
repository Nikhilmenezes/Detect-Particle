# import the necessary packages
import argparse
import imutils
import cv2
import numpy as np


# construct the argument parse and parse the arguments
#ap = argparse.ArgumentParser()
#ap.add_argument("-i", "--image", required=True,help="path to the input image")
#args = vars(ap.parse_args())

# load the image
#image = cv2.imread(args["image"])


name = raw_input("Enter the image path/name : ")
image = cv2.imread(name)


kernel = np.ones(shape=(5, 5),dtype=np.uint8)
image= cv2.erode(image,kernel=kernel,iterations=8)
image = cv2.dilate(image,kernel=kernel,iterations=8)
image= cv2.erode(image,kernel=kernel,iterations=4)


gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]


areas =[]

# find contours in the thresholded image
#cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
disparity, cnts, hierarchy = cv2.findContours(thresh.copy(),mode=cv2.RETR_LIST,method=cv2.CHAIN_APPROX_SIMPLE)
#cnts = imutils.grab_contours(cnts)

# loop over the contours
for i in range(0, len(cnts)):
    areas.append(cv2.contourArea(cnts[i]))

TotalArea = 0

for i in range(0, len(cnts)):
    TotalArea = TotalArea + areas[i]
    print 'Area', (i + 1), ':', areas[i]


print "Total Particles is {} ".format(len(cnts))
print "Total Area is {} ".format(TotalArea)
print "My {} is {}".format("sister","beautiful")
#To Detect all Particles by taking its center marking a green circle aroud it
#for c in cnts:
	# compute the center of the contour
#	M = cv2.moments(c)
#	cX = int(M["m10"] / M["m00"])
#	cY = int(M["m01"] / M["m00"])
	# draw the contour and center of the shape on the image
#	cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
#	cv2.circle(image, (cX, cY), 7, (255, 255, 255), -1)
#	cv2.putText(image, "center", (cX - 20, cY - 20),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

	# show the image
#	cv2.imshow("Image", image)
#cv2.waitKey(0)

