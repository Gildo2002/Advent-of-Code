from itertools import groupby

value = "3113322113"
time = 50

for i in range(time):
    lista = [(c, len(list(cs))) for c, cs in groupby(value)]

    value = ""

    for i, j in lista:
        value += str(j) + str(i)

print(len(value))
