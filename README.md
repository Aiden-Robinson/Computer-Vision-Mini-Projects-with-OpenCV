# Learning-OpenCV
Over the span of a few weeks I took the time to learn some tools in the OpenCV library. I will be sharing my learnings with a brief explanation of each concept

Skills: 

## Loading an Image File
`img= cv2.imread('Assests/albumcover1.png',1)` reads in an image as originally saved (a 0 would indicate greyscale)

`img= cv2.resize(img,(0,0), fx= 2, fy=2)` resizes the image; doubling the width and height

`cv2.imwrite('new_img.png', img)` saves the modified image to files

<img width="350" height="350" src="https://user-images.githubusercontent.com/106715980/179331218-946c57c3-526a-443d-9128-52c61a97a35c.png">

## Understanding Images as NumPy Arrays of Pixels
`print(img[0])` shows the first row of pixels. They are zeros because the first pixels are black thus BGR= (0,0,0). (First row is longer than this)

![image](https://user-images.githubusercontent.com/106715980/179334746-369400f8-cf7b-4c4b-9030-005851d728b1.png)


`print(img.shape)` gives the height, width, and channel of an image. (Channel is how many values are representing each pixel i.e RBG is 3)
![image](https://user-images.githubusercontent.com/106715980/179334360-76d2f96b-0f3b-44aa-88a9-eca40cb92866.png)

`tag= img[50:100, 200:250]` chunks our a group of pixels in the image

`img[100:150,0:50]= tag` places this chunk somewhere else in the image

<img width="350" height="350" src="https://user-images.githubusercontent.com/106715980/179334876-f0748b14-8aae-44fd-a16e-17ed539e66e2.png">

## Capturing the Webcam
`cap= cv2.VideoCapture(0)` captures the webcam

`ret, frame= cap.read()` saves webcame information to a constantly updates an image called frame

`cv2.imshow('frame', frame)` outputs this information in a new window

## Drawing Shapes and Text
`img= cv2.line(frame,(0,0), (width, height), (255,0,0), 10)` draws a line on a certain image specifying the starting coodinates, ending coordinates, the BGR colour, and line thickness

`img= cv2.rectangle(img, (100,100),(200,200),(0,0,255),-1)` draws a rectangle on a certain image specifying the top left coordinates, bottom right coordinates, the BGR colour and thickness

`img= cv2.circle(img, (300,300), 60, (0,255,0),-1)` draws a circle on a certain image specifying the starting coordinates, the radius, the BGR colour, and the thickness

`img= cv2.putText(img, 'Aiden is Great', (200,height-10), font,2, (255,255,255), 5, cv2.LINE_AA )` draws text in at a certain coordinate with a defined font, font magnification, BGR colour, thickness, and line type

<img width="400" height="350" src="https://user-images.githubusercontent.com/106715980/179877403-775116cb-9f03-4e84-8d04-e8a0972376a5.png">

