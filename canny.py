import cv2

image = cv2.imread("book.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# canny edge detection
def canny(gray):
    return cv2.Canny(gray, 100, 200)

canny = canny(gray)

cv2.imshow("canny", canny)
cv2.waitKey()