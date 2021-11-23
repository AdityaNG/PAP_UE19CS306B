from socket import *

serverName = 'localhost'
serverPort = 5000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
print("Client connected to server!")

while True:
    message = input(">> ")
    clientSocket.send(message.encode())
    sentenceReceived = clientSocket.recv(2048).decode()
    print(f">> {sentenceReceived}")
    if(message == 'q'): 
        print("Closing connection...")
        clientSocket.close()