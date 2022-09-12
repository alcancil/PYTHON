#realizando a importação da biblioteca napalm. Importando a parte dos drivers de rede
import napalm
from napalm import get_network_driver
import json

#criando a variavel driver que vai se conectar a um dispositivo ios
driver = napalm.get_network_driver("ios")

device = driver(
    hostname="192.168.0.101",
    username="cisco",
    password="cisco",
    optional_args={"port": 22}
)

#Realizando a conexão com o dispositivo. (variável.open())
device.open()

#Criação da variavel output. Essa variavel recebe o get_facts que é semlhante ao comando show version no cisco ios
output = device.get_facts()
#mostrando o resultado em tela
#dessa maneira, não é muito legível
print(output)

print()
print()

#mostrando o resultado em tela de forma amigável
print(json.dumps(output, indent=4))

print()
print()

#mostrando em tela todas as interfaces
output = device.get_interfaces()
print(json.dumps(output, indent=4))

print()
print()

#mostrando em tela os contadores das interfaces
output = device.get_interfaces_counters()
print(json.dumps(output, indent=4))

print()
print()

#mostrando em tela a tabela arp
output = device.get_arp_table()
print(json.dumps(output, indent=4))