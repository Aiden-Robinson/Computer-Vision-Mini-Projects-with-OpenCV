import cv2
import random

img= cv2.imread('Assests/albumcover1.png',1)
print(img[0]) # gives the height, width, and channels of an image

tag= img[50:100, 200:250] # chunks out a group of pixels in the image

img[100:150,0:50]= tag #places this chunk somehwere else in the image

img=cv2.resize(img, (600,600))

cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
