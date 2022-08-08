#Criando 5 vlans de uma vez no switch 02

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

#loop - criando as vlans
#é necessário converter a string vlans de texto para ascii
tn.write(b"conf t\n")
for vlans in range (10,16):
    #criando as vlans
    tn.write(b"Vlan " + str(vlans).encode('ascii') + b"\n")
    #nomeando as vlans
    tn.write(b"name Site_" + str(vlans).encode('ascii') + b"\n")

tn.write(b"end\n")
tn.write(b"write\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))