#Exemplo de como funciona a bibliotec Telnet (Telnetlib)
#instalar a biblioteca ==>> pipe install telnetlib
#exemplo tirado do site da linguagem python : https://docs.python.org/3/library/telnetlib.html
#Na linha #tn.read_until(b"login: "), trocar de login para Username se não funciona

import getpass
import telnetlib

HOST = "192.168.0.101"
user = input("Digite o seu usuario: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
#tn.read_until(b"login: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"terminal monitor\n")
tn.write(b"debug telnet\n")
tn.write(b"conf t\n")
tn.write(b"int loopback 0\n")
tn.write(b"ip address 1.1.1.1 255.255.255.0\n")
tn.write(b"shut\n")
tn.write(b"no shut\n")
tn.write(b"end\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))