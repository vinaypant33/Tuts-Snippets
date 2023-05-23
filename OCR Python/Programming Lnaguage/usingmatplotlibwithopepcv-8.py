import cv2 
from matplotlib import pyplot as plt



img  = cv2.imread('paper.jpg' , -1)
cv2.imshow('image' , img)

''' Matplotlib shows the image in RGB format while the cv shows the image BGR format so we have to change the format of the image '''

# img  = cv2.cvtColor(img , cv2.COLOR_BAYER_BG2RGB)

plt.imshow(img)
plt.show()

''' Some morpohological transformations are the simple operations based on the Image shape and are performed in the binary image and there are two things
which are reuqired for the transformations

learn about transformations and  how to use them and make demo programs for the same


erosion and other techniques to check and learn 


'''


cv2.waitKey(0)
cv2.destroyAllWindows()