# import library
import cv2 as cv
# load image
img = cv.imread("lena.png")
cv.imshow("Original Lena", img)
cv.waitKey(0)

# draw the rectangle
cv.rectangle(img, (50, 50), (200, 200), 
            (255, 0, 0), 3)
cv.imshow("Rectangle", img)
cv.waitKey(0)