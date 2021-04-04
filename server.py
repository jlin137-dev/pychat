import socket
from time import sleep

HOSTNAME = socket.gethostname()

IP_ADDRESS = socket.gethostbyname(HOSTNAME)

HOST = "0.0.0.0" #IP_ADDRESS
PORT = 3000

BUFFER_SIZE = 1024

message = ""

#list of connections to server
connections = list()

def send(msg):
    # goes through connections to server
    for ip in connections:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            #setting time out to 0.1 of a second so incase chatwatcher isn't active it won't stop
            s.settimeout(0.1)
            s.connect((ip, 3001))
            #sending mesage
            s.send(msg.encode())
            s.close()
        except:
            #remove the ip if connection can't be established to it
            connections.remove(ip) 
    

print("Starting up server...")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(5)

print(f"Server has been initiated on  {IP_ADDRESS}:{PORT}...\n")
while True:
    client_connection, client_address = s.accept()

    request_data = client_connection.recv(BUFFER_SIZE)

    message = request_data.decode("utf-8")

    print(message)
    #if the ip of the connection isn't in the conections list it will add it
    if not client_address[0] in connections:
        connections.append(client_address[0])

    send(message)
    message = ""

s.close()
