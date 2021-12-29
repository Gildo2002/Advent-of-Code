import numpy as np
import ast
from tabulate import tabulate as tb

def replace_value(val:str):
    val = val.replace("\\","\\\\")
    val = val.replace("\"","\\\"")
    return ('"' + val + '"')

array = np.loadtxt('Input/Day08.txt',dtype=str,delimiter='\n')
S_tot = E_tot = 0

for i in range(np.shape(array)[0]):
    S_tot += len(array[i])
    E_tot += len(replace_value(array[i]))

print(E_tot -S_tot)

