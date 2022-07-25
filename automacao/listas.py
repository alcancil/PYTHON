#Aprendizado sobre listas
amigos = ['Marco', 'Pedro', 'Adriana', 'Karina', 'Julia']

#imprimir toda a lista
print(amigos)
#imprimir somente um ítem da lista. A contagem em python começam e ZERO
print(amigos[2])
#imprimir de traz pra frente. Ai não começa da posição ZERO e sim da posisção 1
print(amigos[-2])
#imprimir porções da lista
#mostrar do indice 1 ao 3
print(amigos[1:4])
#mostrar a lista a partir do indice 2
print(amigos[2:])
#modificando itens da lista temporariamente
amigos[1] = 'Alexandre'
print(amigos)