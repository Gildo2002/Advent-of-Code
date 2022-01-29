import json
from pickle import UNICODE

def sum_of_item(value,skip = False):

    if isinstance(value,list):
        return sum([sum_of_item(i,skip) for i in value])

    if isinstance(value,dict):
        if skip and 'red' in value.values():
            return 0
        else:
            return sum([sum_of_item(i,skip) for i in value.values()])

    if isinstance(value,int):
        return value

    return 0


with open('Input/Day12.json') as R:
    data = json.load(R)

print(sum_of_item(data))
print(sum_of_item(data,skip=True))
