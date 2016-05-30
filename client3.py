from socket import *

from threading import Thread

import sys



HOST = ''

PORT = 8888

ADDR = (HOST, PORT)

Sock = socket(AF_INET, SOCK_STREAM)

Sock.connect(ADDR)


data = []
def recv():
	for i in range ( 0 ,4 ):

        	data.append( Sock.recv(1024) )

        	if not data[i]: sys.exit(0)
        	if i==0:
        		print '1..sana'
		elif i==1:
                	print '2..Ayesha'
        	elif i==2:
                	print '3..Sehrish'
        	elif i==3:
                	print '4..Iqra'
print ('enter the client number( 1 , 2 , 3 , 4 ) which you want to communicate$')
n = raw_input('>> ')

	for i in range (0 , 4):

       		if( n == 1):
                	sock.send(data[0])
        	elif(n == 2):
                	sock.send(data[1])
        	elif(n == 3):
                	sock.send(data[2])
        	elif(n == 4):
                	sock.send(data[3])
Thread(target=recv).start()
#def send():
while True:
	dat = raw_input('>---->>>>> ')
        Sock.send(dat)
#Thread(target=send).start()
Sock.close()


