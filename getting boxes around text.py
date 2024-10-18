import cv2
import pytesseract
from pytesseract import Output

img = cv2.imread("book.jpg")

d = pytesseract.image_to_data(img, output_type=Output.DICT)
print(d.keys())

h, w, c = img.shape
boxes = pytesseract.image_to_boxes(img)
for b in boxes.splitlines():
    b = b.split(' ')
    img = cv2.rectangle(img, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 1)

cv2.imshow("img", img)
cv2.waitKey()