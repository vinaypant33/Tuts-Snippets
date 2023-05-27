import cv2 
import numpy as np 
from matplotlib import pyplot as plt

img  = cv2.imread('paper.jpg' , cv2.IMREAD_GRAYSCALE)

titles = ['image']
images =  [img]

for i in range(1):
    plt.subplot(1 , 1 , i+1) , plt.imshow(images[i] , 'gray')
    plt.title(titles[i])
    plt.xticks([] , plt.yticks([]))


plt.show()



''' 
Doing the morphological transformations : They are normally performed on binary images and stucturing elements of kernel 
which decided the operation based on the image shape and performed in the binary shapes 

Homogenous filter and in this each outoput pixel is the mean of this 

Check he dummy code for the low pass filters and high pass filters too


'''