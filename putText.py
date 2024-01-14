# Import libraries
import cv2 as cv
# Load image
img = cv.imread('lena.png')
cv.imshow("Original Lena", img)
cv.waitKey(0)
# Text
text = "LENA"
# Using cv2.putText() method
img = cv.putText(img, text, (50, 50), 
        cv.FONT_HERSHEY_PLAIN , 
        3, (255, 0, 0), 2)
cv.imshow("Image", img)
cv.waitKey(0)