import socket
from time import sleep

HOST = input("Enter IP adress of server: ")

PORT = 3000

BUFFER_SIZE = 1024

#check if server is online
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if not s.connect_ex((HOST, PORT)) == 0:
    print(f"Cannot connect to {HOST}:{PORT}")
    #waits 3 seconds before exiting
    sleep(3)
    exit()
s.close()

USERNAME = input("Pick a username: ")
#join message
MESSAGE = f"{USERNAME} has entered the realm!"

def Send_message():
    global MESSAGE
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.send(MESSAGE.encode())
    MESSAGE = USERNAME + ": " + input("Insert text to send to server: ")
    s.close()

print("Entering chatroom...")
while True:
    Send_message()
