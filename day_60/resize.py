import cv2 as cv 

video= cv.VideoCapture('Videos/dog.mp4')

def rescaleImg(frame,scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int (frame.shape[0]*scale)

    dim=(width,height)

    return cv.resize(frame,dim,interpolation=cv.INTER_AREA)

while True:
    isTrue , frame = video.read()
    resize = rescaleImg(frame)
    cv.imshow('video',frame)
    cv.imshow('video1',resize)

    if cv.waitKey(20) and 0xFF==ord('d'):
        break

video.release()
cv.destroyAllWindows()
