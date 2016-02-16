__author__ = 'Vignesh'
from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM)
serverPort = 8800
serverSocket.bind(('',serverPort))
serverSocket.listen(3)
while True:
	print 'Server Ready'
	connectionSocket, addr = serverSocket.accept()
	try:
		message = connectionSocket.recv(1024)#Fill in start #Fill in end 
		print "message: \n", message
		filename = message.split()[1]
		f = open(filename[1:])
		outputdata = f.read() 
		connectionSocket.send("HTTP/1.1 200 OK")
		for i in range(0, len(outputdata)):
			connectionSocket.send(outputdata[i])
		connectionSocket.close()
	except IOError:
		connectionSocket.send("HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n<!doctype html><html><body><h1>404 Not Found<h1></body></html>")
		connectionSocket.close()
serverSocket.close()