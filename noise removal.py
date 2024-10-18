import cv2

image = cv2.imread("book.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# noise removal
def noise_removal(gray):
    return cv2.GaussianBlur(gray, (5, 5), 0)

gauss = noise_removal(gray)

gray = gauss
cv2.imshow("gauss", gauss)
cv2.waitKey()