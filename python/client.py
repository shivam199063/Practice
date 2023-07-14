import socket

s = socket.socket()
# while True:

   
s.connect( ("15.206.122.116",1234) )
   
data = b"echo 'Jai shree Ram"
s.send(str(data))
s.recv()
s.close()
