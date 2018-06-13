import numpy as np
import cv2
img=cv2.imread('news.jpeg',0);
print(img);
cv2.namedWindow('image',cv2.WINDOW_NORMAL);#Auo resize is default

cv2.imshow('image',img);#->image is window name and img is object name
#->waitkey help to hold the system
cv2.waitKey(0)
#->any key press then destroyAllWindow()
##Write image in harddisk
imwrite("<new name of file>",image object)
cv2.imwrite('jims.png',img)
k=cv2.waitKey(0);
print(k)
if k==27:#wait for ESC key to exit
    cv2.destroyAllWindows();
elif k==ord('s'):#wait for 's' key to save and exit
#->create the image in working directory   
    cv2.imwrite('news12233.png',img);
    cv.destroyAllWindows();
