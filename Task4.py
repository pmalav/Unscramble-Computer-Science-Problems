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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

receive_calls = []
texts_list = []
telmark_nums = []

for rec_num in calls:
    if rec_num[1] not in receive_calls:
        receive_calls.append(rec_num[1])

for text in texts:
    if text[0] not in texts_list:
        texts_list.append(text[0])
    if text[1] not in texts_list:
        texts_list.append(text[1])

for call_num in calls:
    if call_num[0][0:3] != '140':
        if (call_num[0] not in receive_calls) and (call_num[0] not in texts_list) and (call_num[0] not in telmark_nums):
            telmark_nums.append(call_num[0])

print(sorted(telmark_nums, key=str))