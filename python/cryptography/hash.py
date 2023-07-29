import hashlib

password="hello"

password= hashlib.md5(password.encode())
print(password.hexdigest())



