#Configurando as interfaces G0/1 e G0/2 dos routers 1, 2 e 3
#Configurando e testando o OSPF nos 3 routers

import getpass
import telnetlib

HOST = "192.168.0.101"

user = input("Digite o seu usuario: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

#Configurando interface giga0/1
tn.write(b"conf t\n")
tn.write(b"interface gi0/1\n")
tn.write(b"ip address 10.100.102.2 255.255.255.252\n")
tn.write(b"no shutdown\n")

#configurando o ospf
tn.write(b"router ospf 100\n")
tn.write(b"network 10.100.102.0 0.0.0.3 area 0\n")
tn.write(b"end\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))