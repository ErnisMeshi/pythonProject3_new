import cv2 as cv

img = cv.imread('cats.jpg')
cv.imshow('Cats', img)
# Averaging
average=cv.blur(img,(3,3))
cv.imshow('Average Blur',average)
# Median Blur (better than two filters above)
median=cv.medianBlur(img,3)
cv.imshow('Median Blur',median)
# Bilateral
bilateral=cv.bilateralFilter(img,10,35,25)
cv.imshow('Bilateral',bilateral)
cv.waitKey(0)