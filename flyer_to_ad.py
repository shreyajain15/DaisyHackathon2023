import PIL
import cv2

import pytesseract
from pytesseract import Output
print("Hello")
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\nikhi\AppData\Local\Programs\Tesseract-OCR\tesseract'
img = cv2.imread('ad1.png')

def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# noise removal
def remove_noise(image):
    return cv2.medianBlur(image,5)
 
#thresholding
def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

gray = get_grayscale(img)
thresh = thresholding(gray)
text = pytesseract.image_to_string(img)

ocr_output_details = pytesseract.image_to_data(img, output_type = Output.DICT, lang='eng')
# Total bounding boxes
n_boxes = len(ocr_output_details['level'])
print(n_boxes)
print(ocr_output_details)
box_size= []
for i in range(n_boxes):
    (x, y, w, h) = (ocr_output_details['left'][i], ocr_output_details['top'][i], ocr_output_details['width'][i], ocr_output_details['height'][i])
    box_size.append((abs(x-w)*abs(y-h)))


print(box_size.index(max(box_size)))
print(text)
