import pytesseract as pyt
import cv2

# Read file img
img = cv2.imread("Image.png")

# Use engine tesseract to convert
pyt.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

#Convert Image to string by method image_to_string in module pytesseract
text = pyt.image_to_string(img)

# Copy text convert to file txt
with open("file.txt", "w") as data:
    data.write(text)