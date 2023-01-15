import PIL
import cv2

import pytesseract
from pytesseract import Output
print("Hello")
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\nikhi\AppData\Local\Programs\Tesseract-OCR\tesseract'
img = cv2.imread('ad_2131.png')
img = cv2.resize(img, None, fx=3, fy=3)


def get_grayscale(image):
     return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# # noise removal
def remove_noise(image):
    return cv2.medianBlur(image,5)
 
# #thresholding
def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
def get_price(ocr_output_details):
        # # Total bounding boxes
    n_levels = len(set(ocr_output_details['line_num']))
    cur_level = 1
    n_boxes = len((ocr_output_details['level']))
    print('lalalalaaaa',n_levels)
    box_size= []
    average=[]
    j=0
    while j <= len(ocr_output_details['level'])-1:
        if ocr_output_details['level'][j]!=5:
            ocr_output_details['level'].pop(j)
            ocr_output_details['text'].pop(j)
            ocr_output_details['line_num'].pop(j)

        else:
            j+=1
    #print(ocr_output_details)
    n= len(ocr_output_details['text'])
    # for i in range(n_levels+1):
    #     for j in range(n):
    #         if ocr_output_details['line_num']==n_levels:
    #             (x, y, w, h) = (ocr_output_details['left'][j], ocr_output_details['top'][j], ocr_output_details['width'][j], ocr_output_details['height'][j])
    #             box_size.append(abs(y-h))

    print('lalalalalalalalalal', ocr_output_details['text'])
    for i in ocr_output_details['text']:
        if any(char.isdigit() for char in i)==True:
            i=i.strip(' ')
            if 'save' in i or 'SAVE' in i or 'Save' in i:
                continue
            if '/' in i:
                i= i.split('/')
                price= int(i[1])/int(i[0])
            if 'for' in i:
                i= i.split('for')
                price= int(i[1])/int(i[0])
            else:
                price=''.join(c for c in i if c.isdigit())
            break

    return price


gray = get_grayscale(img)
thresh = thresholding(gray)
text = pytesseract.image_to_string(img)

print('text', text)

ocr_output_details = pytesseract.image_to_data(img, output_type = Output.DICT, lang='eng')
price = get_price(ocr_output_details)
print('price', price)

import csv
import enchant


data =text

for value in data:
    if value.isalpha() == False and value != ' ':
        data = data.replace(value,'')

data_information = data.split()
delete_list = []
for value in data_information:
    if len(value) <= 2:
        delete_list += [value]

    elif value.islower() == True:
        delete_list += [value]

for value in delete_list:
    data_information.remove(value)

str_data = ""
for word in data_information:
    str_data += word + " "
str_data= str_data.lower()
print(str_data)
with open("dataset_retail.csv", "r") as csv_file:
    distance = 10000000
    object_details = ""
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        str_title = row[0]
        str_title = str_title[10:len(str_title) - 1]
        calculated_value = enchant.utils.levenshtein(str_title, str_data)
        if (calculated_value < distance):
            distance = calculated_value
            object_details = row
            
print(object_details)
price =  float(price)  
print(object_details)      
our_price = float(row[1].strip(' ').strip('"price":'))
if price/our_price >20:
    price= price/100

if price<our_price:
    print('Lower prices of', row[0].strip(' {"name": '), 'to', price)

        



#for word in data_information:
    




