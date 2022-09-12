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

#declarando a variavel R02 que ira conter o host R02
R02 = ConnectHandler(
    device_type = 'cisco_ios',
    host = '192.168.0.102',
    username = 'cisco',
    password = 'cisco',
)

#declarando a variavel R03 que ira conter o host R03
R03 = ConnectHandler(
    device_type = 'cisco_ios',
    host = '192.168.0.103',
    username = 'cisco',
    password = 'cisco',
)

#Criando a variável para conexão ao host R01
#conectar = ConnectHandler(**R01)
#imprimir em tela a saida dos comandos no host R01
#output = conectar.send_command("show ip int br")

#Conectar nos 3 routers e depois mostrar o prompt. Logo em seguida, desconectar
for routers in (R01, R02, R03):
    print(routers.find_prompt())
    routers.disconnect()

print('Script finalizado com sucesso!!!!')