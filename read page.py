import cv2
import pytesseract

def image_to_text(image_path, output_file):
    # Load image
    image = cv2.imread("book.jpg")

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Thresholding is applied to improve the recognition rate
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # OCR using Tesseract
    custom_config = r'--oem 3 --psm 6'
    text = pytesseract.image_to_string(thresh, config=custom_config)

    # Writes the recognized text to the file
    with open(output_file, 'w') as file:
        file.write(text)


if __name__ == "__main__":
    image_path = 'book.jpg'
    output_file = 'output.txt'
    image_to_text(image_path, output_file)
    print("Text extracted and saved to", output_file)