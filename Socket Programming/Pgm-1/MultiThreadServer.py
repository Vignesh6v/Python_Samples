__author__ = 'Vignesh'

from socket import *
import threading

class ClientThread(threading.Thread):
	def __init__(self, connect, address):
		threading.Thread.__init__(self)
		self.connectionSocket = connect
		self.addr = address
	def run(self):
		while True:
			try:
				message = connectionSocket.recv(1024)
				if not message:
					break
				print "message: \n", message
				filename = message.split()[1]
				f = open(filename[1:])
				outputdata = f.read() 
				connectionSocket.send("HTTP/1.1 200 OK")
				for i in range(0, len(outputdata)):
					connectionSocket.send(outputdata[i])
			except IOError:
				connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n")

if __name__ == '__main__':
	serverSocket = socket(AF_INET, SOCK_STREAM) 
	serverPort = 8800
	serverSocket.bind(('',serverPort))
	serverSocket.listen(3)
	threads=[]
	while True:
		print 'Server Ready'
		connectionSocket, addr = serverSocket.accept()
		client_thread = ClientThread(connectionSocket,addr)
		client_thread.start()
		client_thread.setDaemon(True)
		threads.append(client_thread)
	serverSocket.close()