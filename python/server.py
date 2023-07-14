import socket

s = socket.socket()

s.bind( ("0.0.0.0",1234) )   #here 0.0.0.0 ka matlab hai jo bhi system ka ip hoga ye bydefault vo hi le lega

s.listen()
conn, clientip = s.accept()

data = conn.recv(1000)


print(x)
print(y)
