import socket
import sys
import random
import os
import time
import errno
from random import randint
from socket import error as socket_error
IP = sys.argv[1]
port = sys.argv[2]
Test = sys.argv[3]
readFile = sys.argv[4]



def Send():
	if int(Test) == 1:
		print "open file"
		f = open(readFile, "r")
		while True:
		
			Seed = randint(0,1000000000)
				
			for i in iter(f):
				Seed = int(i.strip('\n') )
				#Seed =  986300252405169304362960275989644611645906120184
				print "seed",Seed
				os.system("date")
				try:
					# Create a TCP/IP socket
					sock = socket.create_connection((IP, int(port)))
					#f.write(Seed + "\n")
				except socket_error:
					print "connection fail\n"
					sys.exit(1)
				
				random.seed(Seed)
				try:
					while True:
							#message = os.urandom(int(Seed))
							message = random.random()
							message = str(message)
								
							#print >>sys.stderr, 'sending "%s"' % message.encode("hex")
				
							sock.send(message)
				except socket_error :
					print "send fail \n"
					continue
    	else:
		f = open(readFile, 'w')
	
		while True:
		
			Seed = randint(0,1000000000000000000000000000000000000000000000000)
			#Seed = 8796
			print "seed", Seed	
		  
			try:
			# Create a TCP/IP socket
			    sock = socket.create_connection((IP, int(port)))
			    f.write(str(Seed) + "\n")
			except socket_error:
			    print "connection fail\n"
			    sys.exit(1)
			
			random.seed(Seed)
			try:
			    while True:
				    #message = os.urandom(int(Seed))
				    message = random.random()
				    message = str(message)
							
				    #print >>sys.stderr, 'sending "%s"' % message.encode("hex")
			
				    sock.send(message)
			except socket_error :
			    print "send fail \n"
			    continue


Send()
