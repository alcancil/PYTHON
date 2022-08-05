#Criando vlans 02 - sales, 03 - eng, 04  - prod nos switches sw01 e sw02

import getpass
import telnetlib

HOST = "192.168.0.112"

user = input("Digite o seu usuario: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"conf t\n")
tn.write(b"vlan 2\n")
tn.write(b"name SALES\n")
tn.write(b"vlan 3\n")
tn.write(b"name ENG\n")
tn.write(b"vlan 4 \n")
tn.write(b"name PROD \n")
tn.write(b"end\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))