from socket import *
from sys import argv

if len(argv) < 2:
    print("Server IP and Port number not specified")
    print("Usage: python3 UDPClient.py <serverIP>:<PortNum>")
    exit(1)

bufferSize = 1024
msgFromClient = "Hello from client"
bytesToSend = str.encode(msgFromClient)

# Client
clientSocket = socket(AF_INET, SOCK_DGRAM) # UDP connection

# Sending message to server
IPAddress, port = argv[1].split(':')
clientSocket.sendto(bytesToSend, (IPAddress, int(port)))
msgFromServer = clientSocket.recvfrom(bufferSize)
print(f"Server: {msgFromServer[0].decode()}")