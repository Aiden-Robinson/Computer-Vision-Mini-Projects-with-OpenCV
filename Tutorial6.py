import numpy as np
import cv2
#this code detects the presence of corners and then draws randomly colored lines

img= cv2.imread('Assests/chessboard.jpg') #imports the image of the chessboard from files
img= cv2.resize(img, (0,0), fx=0.3, fy= 0.3)
gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)#the corner detection algorithm requires the image to be in greyscale

corners= cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)# source image, number of corners, minimum confidence in guess 0-1 scale, minimum euclidian distance between points
corners= np.int0(corners) #converts to a readiable dsys

for corner in corners: #iterates through array of floating point values
    x,y= corner.ravel() #ravels it to just integers. Assigns x and y coorindates from the new array
    cv2.circle(img, (x,y),5, (255,0,0),-1)# draws a blue circle on all of the corner detections

#this part mkaes the randomly coloured lines between corners
for i in range (len(corners)):
    for j in range (i+1, len(corners)):
        corner1= tuple(corners[i][0])
        corner2= tuple(corners[j][0])
        color=tuple(map(lambda x: int(x),np.random.randint(0,255, size=3)))
        cv2.line(img, corner1, corner2,color,1)

cv2.imshow('Frame', img)
cv2.waitKey(0)
cv2.destroyAllWindows()



