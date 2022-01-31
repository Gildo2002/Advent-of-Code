from itertools import permutations
from re import L

def Total_Happiness(me = False):

    arr = {}
    person = set()
    x = [0, 2, 3, 10]

    with open('Input/Day13.txt') as R:
        for line in R.readlines():

            data = line.split()
            value = 0

            p_one = data[x[0]]
            p_two = data[x[3]]

            ope = data[x[1]]
            if ope == 'gain':
                value = int(data[x[2]])
            else:
                value = -int(data[x[2]])

            person.add(p_one)

            arr.update({p_one + p_two: value})

    if me:
        for i in person:
            arr.update({'me' + i: 0})
            arr.update({i + 'me': 0})
        person.add('me')

    calculate_happiness(arr,person)

def calculate_happiness(arr,person):

    optime_pos = 0

    list_permutations = permutations(person)

    for i in list_permutations:
        suma = 0
        for j in range(0, len(i) - 1):

            suma += arr[i[j] + i[j+1]]
            suma += arr[i[j+1] + i[j]]

        suma += arr[i[-1] + i[0]]
        suma += arr[i[0] + i[-1]]

        if suma > optime_pos:
            optime_pos = suma

    print(optime_pos)

Total_Happiness()
Total_Happiness(True)