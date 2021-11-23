# UDP: Connectionless, unreliable, low overhead, fast
from socket import *

localIP = gethostbyname(gethostname()) # Obtain the current IP address of the computer
localPort = 20000
bufferSize = 1024
msgFromServer = "Hello from server"
bytesToSend = str.encode(msgFromServer)

# Server
serverSocket = socket(AF_INET, SOCK_DGRAM) # UDP connection
serverSocket.bind((localIP, localPort))

print(f"UDP server listening at {localIP}:{localPort}...")
print("Pass this IP address and Port Number as arguments to the client program.")

while True:
    bytesAddressPair = serverSocket.recvfrom(bufferSize)
    print(bytesAddressPair)
    message = bytesAddressPair[0]
    address = bytesAddressPair[-1]
    print(f"{address[0]}:{address[1]} : {message.decode()}")

    # Send response
    serverSocket.sendto(bytesToSend, address)