import cv2
import numpy as np 


events  = [i for i in dir(cv2) if 'EVENT' in i] ## Used to check the number of events in cv2
print(events)


def click_event(event , x,  y ,flags  , params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x , ' , ' , y)
        font  = cv2.FONT_HERSHEY_SIMPLEX
        strXY = str(x) + ',' + str(y)
        cv2.putText(img , strXY , (x , y) , font , 1 , (255,255,0) , 2 )
        cv2.imshow('image' , img)
        ## For the right button clicks we can also make the use of  RButton event
        

img  = np.zeros((512 , 512 , 3) , np.uint8)
cv2.imshow('image'  ,img)


cv2.setMouseCallback('image' , click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()