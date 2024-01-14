import cv2 as cv
# load the image
img = cv.imread("lena.png")
# display the image
cv.imshow("Original Image", img)
cv.waitKey(0)