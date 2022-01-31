

def Calculate_speed():

    Reindeer = {}
    x = [0,3,6,13]
    limit= 2503
    lista = []

    with open('Input/Day14.txt') as R:
        for line in R.readlines():
            vals = line.split()

            name    = vals[x[0]]
            speed   = int(vals[x[1]])
            tim     = int(vals[x[2]])
            rest    = int(vals[x[3]])

            Reindeer.update({name:[speed,tim,rest]})

    for i in Reindeer.items():

        n = i[1]
        route = n[1] + n[2]
        go = n[1]
        seg = 0

        for t in range(0,limit):

            if t > limit:
                break

            if t < go:
                seg += 1
            elif t <= route:
                continue
            elif t > route:
                go += n[1] + n[2]
                route += n[1] + n[2]
                seg += 1

        print(i[0],n[0] * (seg * n[1]))
        lista.append(n[0] * (seg * n[1]))

    print(max(lista))

Calculate_speed()

