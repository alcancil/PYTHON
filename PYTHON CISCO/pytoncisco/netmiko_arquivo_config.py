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

#abrindo arquivo de configurações
with open('config_router_file') as file:
    config_line = file.read().splitlines()

lista_routers = [R01, R02, R03]

#Conectar nos 3 routers, aplicar as configs do arquivo de configs e disconectar
for routers in lista_routers:
    configure = routers.send_config_set(config_line)
    print(configure)
    routers.disconnect()

print('Script finalizado com sucesso!!!!')