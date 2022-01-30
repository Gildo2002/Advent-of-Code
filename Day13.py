import itertools

def load_values():
    
    x = [0,2,3,10]

    with open('Input/Day13.txt') as R:
        lines = R.readlines()

    arr = {}
    person = set()

    for line in lines:

        data = line.split()

        person1 = data[x[0]]
        ope = data[x[1]]
        value = int(data[x[2]])
        person2 = data[x[3]]

        person.add(person1)

        arr.update({person1+person2:[ope,value]})

    return arr,person

arr, person = load_values()
optime_pos = 0

for i in itertools.permutations(person):
    suma = 0
    for j in range(0,len(i)-1):
        sitting = i[j] + i[j+1]
        print(sitting)
        value = arr[sitting]
        if value[0] == 'gain':
            suma += value[1]
        else:
            suma -= value[1]

    if suma > optime_pos:
        print(suma)
        optime_pos = suma
    break

print(optime_pos)

