from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

print("The servers is ready to receive")
connectionSocket, addr = serverSocket.accept()

while True:
    message = connectionSocket.recv(2048).decode()
    modifiedMessage = message.upper()
    connectionSocket.send(modifiedMessage.encode() )

connectionSocket.close()
