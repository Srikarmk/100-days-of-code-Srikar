import cv2 as cv

img= cv.imread('Photos/park.jpg')

cv.imshow('org',img)
#grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow('Gray',gray)
#blur
blur =cv.GaussianBlur(img ,(3,3),cv.BORDER_DEFAULT)
cv.imshow('blur',blur)

#edges cascade
edge_cas=cv.Canny(blur,200,100)
cv.imshow('edge_case',edge_cas)

#dilation 
dil=cv.dilate(edge_cas,(7,7),iterations=3)
cv.imshow('dilation done',dil)

#erosion 
erode=cv.erode(dil,(7,7),iterations=3)
cv.imshow('eroded',erode)
cv.waitKey(0)