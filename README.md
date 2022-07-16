# Learning-OpenCV
Over the span of a few weeks I took the time to learn some tools in the OpenCV library. I will be sharing my learnings with a brief explanation of each concept

## Loading an Image File
`img= cv2.imread('Assests/albumcover1.png',1)` reads in an image as originally saved (a 0 would indicate greyscale)

`img= cv2.resize(img,(0,0), fx= 2, fy=2)` resizes the image; doubling the width and height

<img width="350" height="350" src="https://user-images.githubusercontent.com/106715980/179331218-946c57c3-526a-443d-9128-52c61a97a35c.png">
