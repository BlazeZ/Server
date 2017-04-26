import socket
import sys
import random
import os
import time
from random import randint
IP = sys.argv[1]
port = sys.argv[2]
readFile = sys.argv[3]


def main():
	f = open(readFile, 'w')
	while True:
		try:
		        #Create a TCP/IP socket
		        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		        #bind the socket to the port
		        server_address = (IP ,int(port))
		        print >> sys.stderr, 'starting up on %s port %s' % server_address
		        sock.bind(server_address)
		        sock.listen(1)

		        while True:
			    Seed = randint(0,1000000000000000000000000000000000000000000000000)
			    f.write(str(Seed) + "\n")
		            #wait for a connection
		            print >> sys.stderr , 'waiting for a connection'
		            connection,client_address = sock.accept()
		            print >> sys.stderr, ' connection from', client_address

		            #Receive the data in small chunks and retransmit it
		            while True:
			    	#data = connection.recv(20)
			        message = random.random()
				message = str(message)
			        print >>sys.stderr, 'received "%s"' % message.encode("hex")
		                print >>sys.stderr, 'sending data back to the client'
		                connection.sendall(message)
		except:
			time.sleep(30)
			continue


main()
