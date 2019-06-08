from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))

print("The servers is ready to receive")
while True:
	message, clientAddress = serverSocket.recvfrom(2048)
	print("Got it!: {}".format(message))
	modifiedMessage = message.decode().upper()
	serverSocket.sendto(modifiedMessage.encode(), clientAddress)
