from subprocess import check_output
import re
from os import system

while True:
    HOST = input("Enter IP adress of server: ")
    #check if is valid
    ip_check = re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$",HOST)
    if ip_check:
        break

def ping():
    while True:
        return_value = check_output(["ping",HOST]).decode()
        ping = re.split(",",return_value)[-1]
        system("cls")
        print(ping.split("= ")[1].strip())

ping()
