import cv2 as cv
img = cv.imread('lena.png')
cv.imshow("Original Lena", img)
cv.waitKey(0)

# Coordinates of face
face = img[256:307, 177:245]
cv.imshow("Face Cropped", face)
cv.waitKey(0)