import cv2

image = cv2.imread("book.jpg")

# get grayscale image
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

gray = get_grayscale(image)

image = gray
cv2.imshow("gray", image)
cv2.waitKey()