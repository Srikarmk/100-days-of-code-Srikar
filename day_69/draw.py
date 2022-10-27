import cv2 as cv 
import numpy as np

canvas = np.zeros((500,500,3),dtype='uint8')  #zeroes((w,h,channels),dtypp='uint8' - datatype of imgs)

#paint the image a color and a square gen 
# canvas[200:300,200:400]=255,0,0   #(b,g,r) [:] - refrences all pixels
# cv.imshow('canvas',canvas)

# draw a rectangle 
cv.rectangle(canvas , (0,0),(250,250),(255,0,0),thickness=2)
cv.rectangle(canvas , (250,250),(500,500),(255,0,0),thickness=-1)  #cv.FILLED

#draw a circle 

cv.circle(canvas,((canvas.shape[1]//2),(canvas.shape[0]//2)),50,(205,125,60),-1)

cv.putText(canvas,'Srikar',(300,200),cv.FONT_HERSHEY_TRIPLEX,1.0,(255,255,255),2)


cv.line(canvas,(0,0),(250,250),(255,255,255),4)
cv.imshow('Canvas',canvas)
cv.waitKey(0)