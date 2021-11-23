from socket import *

# Server
serverPort = 5000
serverSocket = socket(AF_INET, SOCK_STREAM) # TCP connection
serverSocket.bind(('', serverPort))
serverSocket.listen(1)                      # Listen to 1 connection
print("Server Ready to Receive!")

connectionSocket, address = serverSocket.accept()

while True:
    sentenceReceived = connectionSocket.recv(2048).decode()
    print(f">> {sentenceReceived}")
    message = input(">> ")
    connectionSocket.send(message.encode())
    if(message == 'q'): 
        print("Closing connection...")
        connectionSocket.close()