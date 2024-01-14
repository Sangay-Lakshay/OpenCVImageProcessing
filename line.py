# import library
import cv2 as cv
# load image
img = cv.imread("lena.png")
cv.imshow("Original Lena", img)
cv.waitKey(0)

# draw the line
cv.line(img, (0, 0), (100, 100), (255, 0, 0), 3)
cv.imshow("Line", img)
cv.waitKey(0)