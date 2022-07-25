#Aprendendo a somar números
num1 = input('Digite o primeiro número (inteiro)  : ')
num2 = input('Digite o segundo  número (inteiro)  : ')
num3 = input('Digite o terceiro número (quebrado) : ')
num4 = input('Digite o quarto   número (quebrado) : ')
result  = num1 + num2
result2 = int(num1) + int(num2)
result3 = float(num3) + float(num4)

#Quando armazenaos um número em uma váriavel, este será aramzenado em forma de string
print(result)
#Para realizar a soma dos números armazenado, é necessário converter eles para números
#Podemos converter para inteiro
print(result2)
#Podemos converter para float
print(result3)