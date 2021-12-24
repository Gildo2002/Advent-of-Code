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


def Count_vowels(val):
    i = 0
    for x in ["a", "e", "i", "o", "u"]:
        if val.count(x) > 0:
            i += val.count(x)
    return i

def Count_double(val):
    i = 0
    for x in set(val):
        if val.count(x*2) > 0:
            i += 1
    return i

def Count_ilegal(val):
    i = 0
    for x in ['ab','cd','pq','xy']:
        if val.count(x) > 0:
            i += 1
            break
    return i


with open("Input/Day05.csv", "r", newline="") as read_obj:
    csv_reader = reader(read_obj)
    for vals in csv_reader:
        list_vals.append(Clear_vals(str(vals)))

for value in list_vals:

    rule_1 = True if Count_vowels(value) > 2 else False
    rule_2 = True if Count_double(value) > 0 else False
    rule_3 = True if Count_ilegal(value) == 0 else False

    print(rule_1,rule_2,rule_3,sep=' ')

    if (rule_1 and rule_2 and rule_3):
        nice_string += 1

print('Nice String: ', nice_string)
