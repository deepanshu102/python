import cv2
import numpy as np
'''
#->matplotlib is used for graphics expension
'''
from matplotlib import pyplot as plt
img=cv2.imread('galaxy.jpeg',cv2.IMREAD_GRAYSCALE);
cv2.namedWindow('image');
cv2.imshow('image',img)
cv2.waitKey(1);
cv2.destroyAllWindows()
