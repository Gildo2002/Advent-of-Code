from csv import reader
from typing import Counter

list_vals = []
string_value = ""
nice_string = 0

def Clear_vals(value):
    value = str.replace(value, "[", "")
    value = str.replace(value, "]", "")
    value = str.replace(value, "'", "")
    value = str.replace(value, " ", "")
    return value

def Count_double(val):
    i =0
    for x in range(0,len(val)):
        for y in range(x+1,len(val)):
            if(y+1 < len(val)):
                if (val[x] + val[y+1] == val[x]*2 and y - x == 1):
                    i += 1
                    break
            else:
                continue
    return i


def Count_pair_double(val):
    i = 0
    for x in range(0,len(val)):
        for y in range(x+1,len(val)):
            if (val[x:].count(val[x] + val[y]) > 1):
                i += 1
                break
    return i

with open("Input/Day05.csv", "r", newline="") as read_obj:
    csv_reader = reader(read_obj)
    for vals in csv_reader:
        list_vals.append(Clear_vals(str(vals)))

for value in list_vals:

    rule_1 = True if Count_pair_double(value) > 0 else False
    rule_2 = True if Count_double(value) > 0 else False

    if (rule_1 and rule_2):
        nice_string += 1

print('Nice String: ', nice_string)
