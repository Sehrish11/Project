
import socket               # Import socket module

s = socket.socket()         
host = socket.gethostname()
port = 6000                # Reserve a port for your service.

s.connect((host, port))
print s.recv(2000)
s.close                     # Close the socket when done
