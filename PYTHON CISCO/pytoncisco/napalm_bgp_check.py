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

output = device.get_bgp_neighbors()
print(json.dumps(output, indent=4))