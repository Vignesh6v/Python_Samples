__author__ = 'Vignesh'
from socket import *
import sys
server_host = sys.argv[1]
server_port = sys.argv[2]
filename = sys.argv[3]
host_port = "%s:%s" %(server_host, server_port)
try:
	client_socket = socket(AF_INET,SOCK_STREAM)
	client_socket.connect((server_host,int(server_port)))
	client_socket.send("HTTP/1.1 200 OK")
except IOError:
	sys.exit(1)
final=""
response_message=client_socket.recv(1024)
while response_message:
	final += response_message
	response_message = client_socket.recv(1024)
client_socket.close()