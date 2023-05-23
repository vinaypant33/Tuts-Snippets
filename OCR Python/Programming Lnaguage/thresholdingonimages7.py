''' it is an segmenting technique used on the images 
used for seperating an object from its background : comparing each pixel of an image from the pre defined value





'''

import cv2 as cv  
import numpy as np 


img  = cv.imread('paper.jpg' , 0)


_ , th1 = cv.threshold(img , 127 , 255 , cv.THRESH_BINARY)
_ , th2 = cv.threshold(img , 127 , 255 , cv.THRESH_BINARY_INV)
_ , th3 = cv.threshold(img  , 127 , 255 , cv.THRESH_TRUNC)  ## Used the threahold for simple thresholding thi sis the simple thresholding

## For the adaptive thresholding we have to use the adaptive thresholding and we cannot choose the region for the image and we cannot make the simple threaholding adapt for the different lighting also ( for diff regions )
## Functions are diff for the adaptive thresholding while the method is the same





cv.imshow('image' , img)
cv.imshow('th1' , th1)
cv.imshow('th2' , th2)

cv.waitKey(0)
cv.destroyAllWindows()