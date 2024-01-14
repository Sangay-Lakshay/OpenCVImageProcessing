import cv2 as cv

img = cv.imread("lena.png")
cv.imshow("Original Image", img)
cv.waitKey(0)

# extract height and width
(h, w) = img.shape[:2]
center = (w // 2, h // 2)

# get the rotation matrix
M = cv.getRotationMatrix2D(center, 90, 1)
rotated = cv.warpAffine(img, M, (w, h))
cv.imshow("Rotated by 45 Degrees", rotated)
cv.waitKey(0)