# Learning-OpenCV
Over the span of a few weeks I took the time to learn some tools in the OpenCV library. I will be sharing my learnings with a brief explanation of each concept

`Skills:` Using Masks, Face and Eye Detection, Object Detection, Corner Detection, , Drawing Shapes and Text, Image Pixel Manipulation, Accessing Webcam, 

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

## Colour Isolation with Masks

`lower_blue= np.array([90,50,50])` and `upper_blue= np.array([130,255,255])` defines 2 colours that will be used in the mask

 `mask= cv2.inRange(hsv, lower_blue, upper_blue)` is a mask meaning it isolates all colours between the two specified ranges of colours
 
 `result= cv2.bitwise_and(frame, frame, mask= mask)` is a function that takes a source image and a second image and blends them together using the mask. The mask is used as a function to determine whether or not it should keep a certain pixel. In our case we only have one image and we don’t want to blend two images together therefore we pass the same image twice.
 
 In this small project, I seperated the blues and greens of my webcam using this tool

<img width="450" height="700" src="https://user-images.githubusercontent.com/106715980/179880041-c94178c2-f212-4ffb-a3ea-3e15487b51f0.png">

## Corner Detection

The image I tried corner detection on was a chess board.

`img= cv2.imread('Assests/chessboard.jpg')` imports the image of the chessboard from filefolder

`gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)` the algorithm requires the image to be in greyscale to work

`corners= cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)` parameters are source image, number of corners, minimum confidence on a 0-1 scale, and minimum euclidian distance between points

`x,y= corner.ravel()` assigns x and y coordinates to where the corners are. The .ravel(0 flattens the array

`cv2.circle(img, (x,y),5, (255,0,0),-1)` draws a circle where all the corners are.

<img width="350" height="350" src="https://user-images.githubusercontent.com/106715980/179884571-6ed2d9e2-8331-47ab-a420-919d0f4c9ed1.png">

I then applied this algorithm to my webcam instead of the chessboard image

<img width="400" height="350" src="https://user-images.githubusercontent.com/106715980/179884856-c6c80031-e400-4843-af81-9100beb2f4e5.png">

## Object Detection

For this example I used an image of soccer players and an image of the ball within the picture as the object to detect. It  very important to resize the images so the soccer ball image is roughly how large it appears in the main image.

Full Image | Target Image
:---:|:---:
<img width="150" height="150" src="https://user-images.githubusercontent.com/106715980/180109807-03b14987-7954-48b8-b6a8-03b71c91a863.jpg"> | <img width="150" height="150" src="https://user-images.githubusercontent.com/106715980/180109789-3296dcb8-7a1f-46d0-9b74-0d7506d53bdf.png">


`methods= [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2. TM_CCORR, cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF,cv2.TM_SQDIFF_NORMED]` are template matching methods from OpenCV

`for method in methods:` iterates through each template matching method

`result= cv2.matchTemplate(img2, template,method)` finds the region of detection 

`min_val, max_val, min_loc, max_loc= cv2.minMaxLoc(result)`  and  `location= max_loc` stores the location of each detecion

`bottom_right=(location[0]+ width, location[1]+ height)` finds the bottom right of the detection so a rectangle can be drawn

Here are all of the template matching algorithms and how well they did in detecting the ball. Pictures are black/white because the algorithm works in greyscale


|TM_CCOEFF | TM_CCOEFF_NORMED| TM_CCORR |
|:---:|:---:|:---:|
|<img width="200" height="150" src="https://user-images.githubusercontent.com/106715980/180112424-38bde2b6-31c1-4f64-b868-f52594031ccb.png"> | <img width="200" height="150" src="https://user-images.githubusercontent.com/106715980/180112463-df3e1c43-1daa-43ac-8cd3-48d00d4240f3.png"> | <img width="200" height="150" src="https://user-images.githubusercontent.com/106715980/180112542-5a88cc01-214d-4fbb-b935-112530135b26.png"> |
|TM_CCOR_NORMED | TM_SQDIFF | TM_SQDIFF_NORMED|
|<img width="200" height="150" src="https://user-images.githubusercontent.com/106715980/180112606-9719edb5-56a1-4cca-8400-dd62e364dc7c.png"> | <img width="200" height="150" src="https://user-images.githubusercontent.com/106715980/180112657-00e449e3-43a0-4d46-95bb-ee27368d1190.png"> | <img width="200" height="150" src="https://user-images.githubusercontent.com/106715980/180112720-015553d6-976c-4bd4-a78c-e1eec7c696f8.png">|

Overall, most of the template matching algorithms worked

## Face and Eye Detection

`Haar Cascade`  is a pretrained classifier that looks at an image and tries to pick out specific features such as the distance between two centroids (eyes for example). It has been trained on hundreds of thousands of images. Each classifier searches for a specific feature

`face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')` imports the face classifer

`eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')` imports the eye classifier

`faces= face_cascade.detectMultiScale(gray,1.3, 5)` detects faces, the parameters are (base image, scale factor, minimum neighbour)

`scale factor` we are giving the haar cascade an image of an arbitrary size, it doesn’t know how big it is. We may have to change the size of the image so the cascade can have something to compare it against to. The recommended value is 1.05 which means shrinking it by 5% each iteration. The smaller the value leads to higher accuracy but a slower performing algorithm

`minNeighbours`  is a parameter specifying how many neighbors each candidate rectangle should have to retain it. The haar cascade returns to us a bunch of positions of potential faces, this is saying how many candidate rectangles I need that are overlapping in a specific area before I determine that this is a face. In other words, how accurate does the algorithm need to be? Higher values result in less detection but with higher quality , 3-6 is a good value for this 

`for (x,y,w,h) in faces:` for each face detection, there are x, y coordinates and width and heights

`cv2.rectangle(frame,(x,y),(x+w, y+h), (255,0,0),5)` draws a rectangel around a detected face

`roi_gray= gray[y:y+h,x: x+w ]` and `roi_color=frame[y:y+h,x:x+w ]` create subspaces in the face rectangle in gray and colour for eye detection to take place

`eyes= eye_cascade.detectMultiScale(roi_gray, 1.3,5)` detects eyes (same parameters as before) and drawing rectangles is the same process

![image](https://user-images.githubusercontent.com/106715980/180119050-d77c0abe-db84-48d9-b3c9-87143bc66fb2.png)

