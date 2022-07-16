import cv2

img= cv2.imread('Assests/albumcover1.png',1) #loads in am image from file directory, 1 means greyscale
img= cv2.resize(img,(0,0), fx= 2, fy=2) #resizint the image; dooubling length and width
#img= cv2.rotate(img, cv2.cv2.ROTATE_90_CLOCKWISE)

cv2.imwrite('new_img.png', img) #saving th rotated image as a new image

cv2.imshow('Image',img) #showing the image
cv2.waitKey(0) #wait until any key is pressed
cv2.destroyAllWindows()




