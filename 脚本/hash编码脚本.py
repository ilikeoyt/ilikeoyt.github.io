import hashlib

hash = hashlib.md5()
hash.update('/fllllllllllllag'.encode('utf-8'))
print(hash.hexdigest())