import cv2 as cv

#Reading imgs
img = cv.imread('Photos/cat.jpg')  # returns a matrix of pixels

cv.imshow('Cat',img)   #opens a window to display img

cv.waitKey(0)   #waits for key press for a few milliseconds 0- infinite amount 

