import cv2
import numpy as np


cap= cv2.VideoCapture(0) #captures the webcam, 0 only matters if there are multiple webcam options

#The following code activates the webcam and splits the images up into 4 smaller screens, two of which are inverted
while True:
    ret, frame= cap.read()
    width= int(cap.get(3)) #3 means the width of the captured webcam (this is from documentation)
    height= int(cap.get(4)) #4 means the width of the captured webcam (this is from documentation)

    image= np.zeros(frame.shape, np.uint8) #duplicates our original output
    smaller_frame= cv2.resize(frame, (0,0), fx= 0.5, fy= 0.5) #shrinks oroginally captured image by halving the width and height which results in 1/4 of the original size
    image[:height//2, :width//2]= cv2.rotate(smaller_frame, cv2.cv2.ROTATE_180) #top left
    image[height // 2:, :width // 2] = cv2.rotate(smaller_frame, cv2.cv2.ROTATE_180) #bottom left
    image[:height // 2, width // 2:] = smaller_frame #top right
    image[height // 2:, width // 2:] = smaller_frame #bottom right

    cv2.imshow('frame', image)

    if cv2.waitKey(1)== ord('q'): #waits for the letter q to be pressed
        break
cap.release()
cv2.destroyAllWindows()

