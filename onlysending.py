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
#check if server is online
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.close()
except:
    print("Cannot establish connection to servers...\nExiting in 3 seconds")
    sleep(3)
    exit()

USERNAME = input("Pick a username: ")

MESSAGE = f"{USERNAME} has joined the chat!"

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