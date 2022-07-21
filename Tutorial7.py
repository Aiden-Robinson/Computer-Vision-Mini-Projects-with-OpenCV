import numpy as np
import cv2

img= cv2.resize(cv2.imread('Assests/soccer_practice.jpg',0),(0,0), fx=0.8, fy=0.8) #importing the whole soccer practice picture
template= cv2.resize(cv2.imread('Assests/shoe.png',0),(0,0), fx= 0.8, fy= 0.8) #importing just the picture of the soccer ball
height,width= template.shape# obtaining the height and width of the soccer ball

methods= [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2. TM_CCORR, cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF,cv2.TM_SQDIFF_NORMED]# template matching methods from OpenCV

for method in methods: #iterating through each detection method
    img2= img.copy() #creating a copy of the image

    result= cv2.matchTemplate(img2, template,method) #matching the two images using the current detection technique
    min_val, max_val, min_loc, max_loc= cv2.minMaxLoc(result) #creating various locations where the detection could occur


    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]: #for these specific algorithms, we want the min location
        location= min_loc
    else:
        location= max_loc #everyth

    bottom_right=(location[0]+ width, location[1]+ height) #finding the bottom right of the detection location so a rectangle can be drawn
    cv2.rectangle(img2, location,bottom_right,255,5)  #drawing the rectangle
    cv2.imshow('Match', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

print(template.shape)
print(img.shape)

