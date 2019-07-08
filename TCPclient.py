from socket import *

serverName = 'localhost'  # 64.90.34.17'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

message = ""
while message != "q":
    message = input('Input lowercase sentence: ')
    clientSocket.send(message.encode())

    modifiedMessage = clientSocket.recv(1024)
    print('From server: ', modifiedMessage.decode())

clientSocket.close()
