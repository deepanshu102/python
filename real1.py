import numpy as np
import cv2
img=cv2.imread('news.jpeg',0);
print(img);
cv2.namedWindow('image');#Auo resize is default
#->Getting image details
#->Shape of the image in pixel
print(img.shape);
#total pixel
print(img.size);
#-> image type like uint8 
print(img.dtype);
#->type of image object
print(type(img));
#->
print(img.ndim);
#->resize the image 
res=cv2.resize(img,(800,1275));
print(res.shape);
#decrease the sizze of image
res2=cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
print(res2.shape);
print(res2.size);
print(res2.size);
print(res2.dtype);
print(type(res2));
print(res.ndim);
cv2.imshow('image',res2);
#hold the screen
cv2.waitKey(0)
cv2.destroyAllWindows();
