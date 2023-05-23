import numpy as np 
import cv2 


img  = cv2.imread('paper.jpg')


print(img.shape)
print(img.size)
print(img.dtype)

b , g, r = cv2.split(img)
img = cv2.merge((b , g , r))

''' Region of intrest '''
ball = img[280:340 , 330:390] #3 The coordinates are used to copy the part of the image
img[273 : 333 , 100 : 160] ## Bal placed on another part too


''' Joining the two Images 

    calling the anothter image the second image should be equal to the size of the first Image 
    add method can be used for the image editing

    we can resie the image too :  cv2.resize(image , (rowsize , columnsize))
    this makes a final merged image. 
    add weighted method : used to give the weight to one more than the another image

    bitwise operations : used to make the masks: 
    

    we can use the hsv color space for the object tracking :  

    


 '''

 ## Make named window to chnage the variables of the image 
cv2.namedWindow('Tracking')

def nothing(x):
    pass

cv2.createTrackbar("LH" , "Tracking" , 0 , 255 , nothing)


cv2.imshow('image'  , img)
cv2.waitKey()
cv2.destroyAllWindows()

''' We can also use the merge method :  the ROI region of interest of the image : 

For that we get the coordinats from the image wherw we have to implement the image types " Numpy indexing features 



'''