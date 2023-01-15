import csv
import enchant


data = """
        e(0 "499

        THE ORGANIC CLEMENTINES 1 5!b bag

        )  o product of spain
"""

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


with open("dataset_retail.csv", "r") as csv_file:
    distance = 0
    object_details = ""
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        str_title = row[0]
        str_title = str_title[10:len(str_title) - 1]
        calculated_value = enchant.utils.levenshtein(str_title, str_data)
        if (calculated_value > distance):
            distance = calculated_value
            object_details = row
            


        



#for word in data_information:
    

