#Criando o backup das configurações dos routers

import getpass
import telnetlib

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
    print("Realizando o backup das configs do ROUTER " + (ip))
    tn = telnetlib.Telnet(HOST)
    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
       tn.read_until(b"Password: ")
       tn.write(password.encode('ascii') + b"\n")
    #fim da conexão telnet
    #pede para serem exibidas as mensagens no console
    tn.write(b"terminal monitor\n")
    #muda o comportamento do tamanho da saida do terminal para infinito. Não usa mais o comando more
    tn.write(b"terminal length 0\n")
    tn.write(b"show run\n")
    tn.write(b"exit\n")

    #leia o conteúdo inteiro que foi passado no tn.write
    ler_config = tn.read_all()
    #grave toda a saida de ler_config em arquivos chamados bkp com permissão write
    save_config = open('bkp-' + HOST, 'w')
    #decodificando os resultados como ascii
    save_config.write(ler_config.decode('ascii'))
    #pressione enter para gravar
    save_config.write('\n')
    #fechando o arquivo
    save_config.close()

print("Backup realizado com sucesso !!!")