import hashlib

for i in range(1,10000000) :
    str_md5 = hashlib.md5(str(i).encode('utf-8')).hexdigest()
    if str_md5[0:6] == '6d0bc1':
        print(i)