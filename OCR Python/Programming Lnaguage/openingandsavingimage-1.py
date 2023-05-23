""" Python can be used for Open CV for computer vision 

Digital images are stored in the form of pixel images matrix and  they are grayscale and coloured Images 
This refers how bright and dark the image is ? 

Numpy is also  used for operating the matrix of the Images



"""

import cv2
from time import sleep



img  = cv2.imread('paper.jpg' , -0) # after the name we can also specify the flag which determines how the images are read  1 Lods color image , 0 loads grayscale Image and  -1 load images including the alpha channel 


print(img) # It displays the image as a matrix
cv2.imshow('image' ,img) ## Shows th image which we can see  

# We will be taking the input of the waitkey and then closing the app based on the Input 

k = cv2.waitKey(0)
if k == 27: ## using the escape key to close the windows
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('Iamimage.png' , img) # Used to copy the image or save the Image
    cv2.destroyAllWindows() ## Closes all windows

# cv2.waitKey(5000) ## Waits for this milliseconds before closing the Image 




