"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

telnum_list = []

for element in texts:
    if element[0] not in telnum_list:
        telnum_list.append(element[0])
    if element[1] not in telnum_list:
        telnum_list.append(element[1])

for element1 in calls:
    if element1[0] not in telnum_list:
        telnum_list.append(element1[0])
    if element1[1] not in telnum_list:
        telnum_list.append(element1[1])

print("There are {0} different telephone numbers in the records.".format(len(telnum_list)))
