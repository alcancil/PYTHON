#Arquivo que mostra o uso de strings

nome = 'Marcos da Silva Sauro'
#String é um texto que pode ser impresso direto na tela ou armazenado dentro de uma variavel
print('Marcos da Silva')
#Pulando uma linha
print('\n')
#Imprimindo uma aspas ( ' ) simples
print('Este é um exemplo de como im primir uma aspas simples \' ')
#Concatenando textos
print(nome + ' tem 19 anos de idade')
#Nas strings é possível se utilizar funções. Basta digitar o nome da string e digitar .nome_da_funcao
#Imprimindo tudo em ciaxa alta, letras maiusculas
print(nome.upper())
#imprimindo tudo em letra minuscula
print(nome.lower())
#Funcao para contar quantos carecteres existem dentro de uma string
#OBS: ele conta espaços vazios também
print('A string NOME tem ',len(nome) , 'caracteres')
#O uso de colchetes [] junto ao nome da variavel indica o uso do indice onde se posicona o cursor ou posicao do carecter
#Obs: a contegem dos caracteres se da a partir do ZERO !!!
print('O decimo caracter da strin nome é o ', nome[10])
#Exemplo de busca de caracteres dentro da string.
#Exemplo: quero saber em que posicao se encontra a cadeia de carcteres da
print("A cadeia de caracteres \'da\' se encontra na posicao", nome.index('da'))
#Exemplo de contagem de caracteres dentro da string
#Quero saber quantas letras a existem dentro da string nome
#OBS: essa função é case sensitive
print('Existem ', nome.count('a') , 'letras a dentro da string nome !!!')
print('Existem ', nome.count('w') , 'letras w dentro da string nome !!!')
print('Existem ', nome.count('s') , 'letras s dentro da string nome !!!')
print('Existem ', nome.count('S') , 'letras S dentro da string nome !!!')