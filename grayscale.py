# import library
import cv2 as cv
# load image
img = cv.imread("Lena.png")
# display the original image
cv.imshow("Original Image", img)
cv.waitKey(0)

# grayscale conversion
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# display the grayscale image
cv.imshow("Grayscale", gray)
cv.waitKey(0)