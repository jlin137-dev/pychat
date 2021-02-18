import socket
from time import sleep
from subprocess import check_output
from os import system
import re

while True:
    HOST = input("Enter IP adress of server: ")
    #check if is valid
    ip_check = re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$",HOST)
    if ip_check:
        break

PORT = 3000

BUFFER_SIZE = 1024

WIFI_NAME = check_output(['netsh', 'wlan', 'show', 'interfaces']).decode('utf-8').split('\n')[19].split(":").pop(1)[1:].replace(" \r","")

CRASHES = 0

HOSTNAME = socket.gethostname()

IP_ADDRESS = socket.gethostbyname(HOSTNAME)

#check if server is online
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.close()
except:
    print(f"Cannot establish connection to {HOST}...\nExiting in 3 seconds")
    sleep(3)
    exit()

def Update():
    while True:
        sleep(0.1)
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((HOST, PORT))
            s.shutdown(socket.SHUT_WR)
            data = s.recv(BUFFER_SIZE)
            print(data.decode("ascii"))
            s.close()
        except:
            pass
def Chat_room() :
    print(f"Succesfully joined chatroom on {WIFI_NAME}.")
    Update()

print("Watching chat room...")
Chat_room()