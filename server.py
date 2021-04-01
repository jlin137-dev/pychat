import socket

HOSTNAME = socket.gethostname()

IP_ADDRESS = socket.gethostbyname(HOSTNAME)

HOST = IP_ADDRESS
PORT = 3000

BUFFER_SIZE = 1024

message = ""
# send through different port so chat watcher still the same but with idffernet port it goes in so don't have same connection problem
def send(ip, msg):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, 3001))
        s.send(msg.encode())
        s.close()
    except:
        pass

print("Starting up server...")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(5)

print(f"Server has been initiated on  {HOST}:{PORT}...\n")
while True:
    client_connection, client_address = s.accept()

    request_data = client_connection.recv(BUFFER_SIZE)

    message = request_data.decode("utf-8")

    print(message)

    client_connection.send(message.encode())
    send(client_address[0],message)
    message = ""

s.close()
