import cv2

image = cv2.imread("book.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# thresholding
def thresholding(gray):
    return cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

thresh = thresholding(gray)

cv2.imshow("thresh", thresh)
cv2.waitKey()