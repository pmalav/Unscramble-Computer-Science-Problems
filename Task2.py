"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

time_dict = {}
for element in calls:
    if element[0] in time_dict:
        time_dict[element[0]] += float(element[3])
    elif element[1] in time_dict:
        time_dict[element[1]] += float(element[3])
    else:
        time_dict[element[0]] = float(element[3])
        time_dict[element[1]] = float(element[3])

telephone_num = max(time_dict, key = time_dict.get)
max_time = max(time_dict.values())

print("{0} spent the longest time, {1} seconds, on the phone during September 2016.".format(telephone_num, max_time))
