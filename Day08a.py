import numpy as np
import ast
from tabulate import tabulate as tb

array = np.loadtxt("Input/Day08.txt", dtype=str, delimiter="\n")

lista = []
S_tot = M_tot = 0

for i in range(np.shape(array)[0]):
    S_tot += len(array[i])
    M_tot += len(ast.literal_eval(array[i]))

print(S_tot - M_tot)
