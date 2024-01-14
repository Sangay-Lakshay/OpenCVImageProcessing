import cv2 as cv
import numpy as np

img = cv.imread('lena.png')
cv.imshow("Original Lena", img)
cv.waitKey(0)

# define the translation matrix
M = np.float32([[1, 0, 25], [0, 1, 50]])
shifted = cv.warpAffine(
    img, M,
    (img.shape[1], img.shape[0])
)
cv.imshow("Shifted", shifted)
cv.waitKey(0)