import socket

IP_ADDRESS = socket.gethostbyname(socket.gethostname())

HOST = "0.0.0.0"

PORT = 3001

BUFFER_SIZE = 1024

message = ""
#functions as a server which listens for connections from the message server
print("Starting up server...")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(5)

print(f"Server has been initiated on  {IP_ADDRESS}:{PORT}...\n")
while True:
    #accept the connection
    client_connection, client_address = s.accept()
    #receive the data
    request_data = client_connection.recv(BUFFER_SIZE)
    #decode data from binary to uft-8
    message = request_data.decode("utf-8")
    #prints message
    print(message)
    #resets message
    message = ""

s.close()
