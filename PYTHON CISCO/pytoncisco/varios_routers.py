#Criando 4 interfaces loopbacks de a 3 nos roteadors r01, r02 e r03 ao mesmo tempo

import getpass
import telnetlib

HOST = "localhost"

user = input("Digite o seu usuario: ")
password = getpass.getpass()

#Criando variável que vai ler os dados de um documento
lista_routers = open('routers_ip')

#para cada endereço ip que estiver na lista faça
for ip in lista_routers:
    #conecte atráves de telnet
    #trava para não ler linhas vazias do arquivo de endereços
    ip = ip.strip()
    HOST = ip
    print("Configurando o roteador " + (ip))
    tn = telnetlib.Telnet(HOST)
    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
       tn.read_until(b"Password: ")
       tn.write(password.encode('ascii') + b"\n")
    #fim da conexão telnet
    #loop - criando as vlans
    #é necessário converter a string vlans de texto para ascii
    tn.write(b"conf t\n")
    for interface_loopback in range (11):
        #criando as loopbacks
        tn.write(b"interface loopback " + str(interface_loopback).encode('ascii') + b"\n")
    tn.write(b"end\n")
    tn.write(b"write\n")
    tn.write(b"exit\n")

    print(tn.read_all().decode('ascii'))

print("Configuração realizada com sucesso !!!")