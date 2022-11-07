import cv2 as cv
import numpy as np
img = cv.imread('Photos/park.jpg')

cv.imshow('Boston' , img)

#translation 
def translate(img,x,y):
    a=[[1,0,x],[0,1,y]]
    transMat = np.float32([x,y])
    dimensions=(img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimensions)
    
translated=translate(img,100,100)
cv.imshow('Traslated',translated)
# -x -> left
# -y->up 
# x->right
# y-> down

cv.waitKey(0)