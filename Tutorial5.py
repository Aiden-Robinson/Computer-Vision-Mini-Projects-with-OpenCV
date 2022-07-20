import cv2
import numpy as np
# in this tutorial we are isolating for blue pixels, we are also showing the mask which is 1 and 0 of where it detects it
cap= cv2.VideoCapture(0)

while True:
    ret, frame= cap.read()
    width= int(cap.get(3))
    height= int(cap.get(4))

    hsv= cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_blue= np.array([90,50,50]) #defining a lower range of blue
    upper_blue= np.array([130,255,255])#defining an upper range of blues

    mask= cv2.inRange(hsv, lower_blue, upper_blue) #defining our mask

    result= cv2.bitwise_and(frame, frame, mask= mask)# the bitwise_and function takes two iomages, the source and a second source image and will blend them together using the mask. the mask determines whether or not a certain pixel should be kept



    cv2.imshow('frame', result)
    cv2.imshow('mask', mask)

    if cv2.waitKey(1)== ord('q'):
        break

cap.release()
cv2.destroyAllWindows()