#Aprendendo funções dentro de listas
numeros = [3, 5, 7, 1 , 2, 12, 100]
amigos  = ['Marcos', 'Peddro', 'Adriana', 'Julio', 'Alexandre']
amigos2 = ['Sonia', 'Joao', 'Raul', 'cintia']
amigos3 = ['alcantara','Machado', 'Joao', 'Raul', 'Pele']
amigos4 = ['alcantara','Machado', 'Joao', 'Raul', 'Pele', 'Pele', 'Pele', 'Pele']

#imprimindo as duas listas ao mesmo tempo
amigos.extend(numeros)
print(amigos)
#adicionando itens a uma lista
amigos.append('Eulalia')
print(amigos)
#inserir um ítem em determinada posição da lista
print(amigos2)
amigos2.insert(1, 'Kleber')
print(amigos2)
#remover itens da lista
amigos2.remove('Sonia')
print(amigos2)
#remover itens da lista através do index
amigos2.pop(1)
print(amigos2)
#verificar qual é o index de algum item da lista
print(amigos3.index('alcantara'))
print(amigos3.index('Pele'))
#contar os ítens de uma lista
print(amigos3.count('Pele'))
print(amigos4.index('Pele'))
#organizando itens da lista
#ordem alfabetica
amigos3.sort()
print(amigos3)
#ordem numerica
numeros.sort()
print(numeros)