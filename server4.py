'''
    Simple socket server using threads
'''
  
import socket
import sys
from thread import *
  
HOST = ''   # Symbolic name meaning all available interfaces
PORT = 5188 # Arbitrary non-privileged port
address = []
client=[]
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'
  
#Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
      
print 'Socket bind complete'
  
#Start listening on socket
s.listen(10)
print 'Socket now listening'
  
#Function for handling connections. This will be used to create threads

def clientthread(conn):
    #Sending message to connected client
    name=conn.recv(1024)
    client.append(name)
    for i in range(len(client)-1):
	address[i].sendall(name +' is Available for chat:')	
    conn.send('Welcome to the server. Available clients are : \n') #send only takes string
    for i in range(len(client)):
	conn.send(client[i].upper()+'\n')
   # infinite loop so that function do not terminate and thread do not end.
    while True:  
        #Receiving from client
	data = conn.recv(1024)
	reply=data		
	for x in range(len(client)):		
		address[x].sendall(reply)
    conn.close()
  

while 1:
    #wait to accept a connection - blocking call
    conn, addr = s.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
    address.append(conn)
    start_new_thread(clientthread ,(conn,))
 	 
s.close()
