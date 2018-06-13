import cv2
cap=cv2.VideoCapture(0);
fourcc=cv2.VideoWriter_fourcc(*'MJPG');
out=cv2.VideoWriter('output.mp4',fourcc,20.0,(600,480));
while(True):
    ret,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    out.write(frame);
    cv2.imshow('frame',gray);#->for color cv2.imshow('frame',frame);
    key=cv2.waitKey(1);
    if(key==ord('q')):
        break;
cap.release()
out.release();
cv2.destroyAllWindows();
