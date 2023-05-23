import cv2
cap = cv2.VideoCapture(0) #3 The index tells the current camera for multiple cameras start with -1 and go higher 
## To show the image from the predefined video we have to provie the video file with the extension in videocapture instead of 0

## To save the videow e can use the video writer : 
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out  = cv2.VideoWriter('outputname.avi' , fourcc , 20.0 , (640,480)) ## name, 4cc code for the video, no of frames per sec , size

''' to check if the video is open we have to check the while loop as : 

while (cap.isopened()) : '''

while True:
    ret , frame  =  cap.read()
    if ret == True:

       ''' we can also read using the properties usign the get cap.get(cv2.CAP_PROP_FRAME_WIDTH) same for the height too
    

    
         '''
    out.write(frame) ## used to write the frame and save the video then

    ## TO chnage the color to the grayscale
    # gray = cv2.cvtColor(frame , cv2.COLOR_BG2GRAY)
    cv2.imshow('frame' , frame) ## We have to chnage the frame to gray to show the grayscale files
    if cv2.waitKey(1) & 0Xff == ord('q'):
        break



cap.release()
out.release()
cv2.destroyAllWindows()

