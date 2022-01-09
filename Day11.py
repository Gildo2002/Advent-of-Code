# a = 97, z = 122

from typing import ChainMap


c = "hepxxzaa"
min = 97
max = 122
lim = len(c) - 2

def increment_letters(lst: list):
    for i in range(-1,-9,-1):
        if lst[i] == chr(max):
                lst[i] = chr(min)
        else:
            lst[i] = chr(ord(lst[i])+1)
            break
    return ''.join(lst)

def valid_pass():
    return r_one() and r_two() and r_three()


def r_one():
    for i in range(lim):
        if ord(c[i]) > max - 2:
            pass
        else:
            chair = (''.join([chr(ord(c[i])+a) for a in range(3)]))
            if c[i:i+3] == chair:
                return True
    return False


def r_two():
    for i in ["i", "o", "l"]:
        if i in c:
            return False
    return True


def r_three():
    x = 0
    for i in ([a+a for a in set(c)]):
        if i in c:
            x += 1
    return x >= 2


while valid_pass() != True:
    c = increment_letters(list(c))

print(c)
