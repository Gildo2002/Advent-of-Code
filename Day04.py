import hashlib as hs
i = 0
key = 'ckczppom'


while(True):
    value = key + str(i)
    md5_hash = hs.md5(value.encode())
    Answer_hash = md5_hash.hexdigest()
    if (Answer_hash[0:6] == '000000'):
        print(i)
        break
    i+=1