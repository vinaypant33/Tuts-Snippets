import numpy as np
import cv2

# img  = cv2.imread('paper.jpg' , 0)

'''  we can also make the image using the numpy zeros method '''

img  = np.zeros([512 ,512 , 3 ] , np.uint8) ## Creating the black image using the height width and other parameters



cv2.imshow('image' , img)

img = cv2.line(img , (10 , 10) , (200,200) , (0,0,255) , 2) ## We can also make the arrowedline and rectangle etc for the same

cv2.imshow('image' , img)
cv2.waitKey(0)
cv2.destroyAllWindows()

