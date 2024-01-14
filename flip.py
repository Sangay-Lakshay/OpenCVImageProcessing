import cv2 as cv
# Load image
img = cv.imread("lena.png")
cv.imshow("Original Lena", img)
cv.waitKey(0)

flipped = cv.flip(img, 0)
cv.imshow("Flipped Horizontally", flipped)
cv.waitKey(0)