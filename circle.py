# import library
import cv2 as cv
# load image
img = cv.imread("lena.png")
cv.imshow("Original Lena", img)
cv.waitKey(0)

# draw the circle
cv.circle(img, (200, 200), 100, (255, 0, 0), 3)
cv.imshow("Circle", img)
cv.waitKey(0)