import numpy as np
import cv2
#->VideoCapture(0) help to record the video
cap=cv2.VideoCapture(0);
a=0
while(True):
    a=a+1;
    ret,frame=cap.read();
    #print(ret);
    #print(frame);
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',gray);
    key=cv2.waitKey(1)
    if(key==ord('q')):
        break
print(a);
cap.release();
cv2.destroyAllWindows()
    
