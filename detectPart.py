import cv2
import numpy




name = raw_input("Enter the image path/name : ")
frame = cv2.imread(name)


frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
ret, frame = cv2.threshold(frame, 127, 255, cv2.THRESH_BINARY)



frame, contours, hierarchy = cv2.findContours(frame, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
areas = []



for i in range(0, len(contours)):

    areas.append(cv2.contourArea(contours[i]))



#print 'Num particles: ', len(contours)


for i in range(0, len(contours)):

    print 'Area', (i + 1), ':', areas[i]


print "Total Particles is {} ".format(len(contours))

cv2.imshow("Frame", frame)
cv2.waitKey(0)
