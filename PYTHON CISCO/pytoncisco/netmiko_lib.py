#realizando a conexão ssh através da biblioteca netmiko

#importando a biblioteca Netmiko
from netmiko import ConnectHandler

#declarando a variavel R01 que ira conter o host R01
R01 = ConnectHandler(
    device_type = 'cisco_ios',
    host = '192.168.0.101',
    username = 'cisco',
    password = 'cisco',
)

#Criando a variável para conexão ao host R01
#conectar = ConnectHandler(**R01)
#imprimir em tela a saida dos comandos no host R01
#output = conectar.send_command("show ip int br")

output = R01.send_command("show ip int br")
print(output)