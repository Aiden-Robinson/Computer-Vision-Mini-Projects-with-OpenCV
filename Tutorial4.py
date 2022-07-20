import numpy as np
import cv2

cap= cv2.VideoCapture(0)

while True:
    ret, frame= cap.read()
    width= int(cap.get(3))
    height= int(cap.get(4))

    img= cv2.line(frame,(0,0), (width, height), (255,0,0), 10) #creates a duplicate image and draws one blue diagonal line. (start coodinates), (end coordinates), (colour), (thickness)
    img = cv2.line(img, (0, height), (width, 0), (255, 0, 0), 10) #drawing another diagonal line
    img= cv2.rectangle(img, (100,100),(200,200),(0,0,255),-1) #drawing a rectangle. (top left), (bottom right), (colour), (thickness)

    img= cv2.circle(img, (300,300), 60, (0,255,0),-1) #draws a circle (starting coordinates), (radius), (colour), (thickness)

    font= cv2.FONT_HERSHEY_SIMPLEX
    img= cv2.putText(img, 'Aiden is Great', (200,height-10), font,2, (255,255,255), 5, cv2.LINE_AA ) # draws text with the coordinates, the font, font magnification, the colour, the thickness and line type

    cv2.imshow('frame', img)

    if cv2.waitKey(1)== ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
