import cv2
import numpy as np

image = cv2.imread("book.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# opening-erosion followed by dilation
def opening(gray):
    kernel = np.ones((3, 3), np.uint8)
    return cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)

opening = opening(gray)

cv2.imshow("opening", opening)
cv2.waitKey()