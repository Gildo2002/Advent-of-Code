from types import DynamicClassAttribute
import numpy as np
from csv import reader

list_vals = []
ins = ['turnon','turnoff','toggle']
toggle = {0:1,1:0}

matriz = np.zeros([1000,1000])

def Clear_vals(value):
    for i in ['[',']',"'",',']:
        value = str.replace(value, i, "")
    value = str.split(value,' ')
    return value

with open("Input/Day06.csv", "r", newline="") as read_obj:
    csv_reader = reader(read_obj)
    for vals in csv_reader:
        list_vals.append(Clear_vals(str(vals)))

for s in list_vals:

    x1,y1,x2,y2 = list(map(int,s[1:]))

    if (s[0] == ins[0]):
        matriz[x1:x2+1, y1:y2+1] = 1
    if (s[0] == ins[1]):
        matriz[x1:x2+1, y1:y2+1] = 0
    if (s[0] == ins[2]):
        matriz[x1:x2+1, y1:y2+1] = np.logical_not(matriz[x1:x2+1, y1:y2+1])

print(np.sum(matriz))

