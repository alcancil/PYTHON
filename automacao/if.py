#aprendendo condições se e se não
acordei_antes_8 = True
acordei_antes_9 = False
acordei_antes_10 = True
fome = True
fome2 = False

#if verdadeiro
if acordei_antes_8:
    print ('Hora de fazer o café da manhã !!!')

#if falso
if acordei_antes_9:
    print('Hora de fazer o café da manhã !!!')
else:
    print('Hora de fazer o almoço !!! Vagabundo !!!!')

#if verdadeiro
if acordei_antes_10:
    print('Hora de fazer o café da manhã !!!')
else:
    print('Hora de fazer o almoço !!! Vagabundo !!!!')

#acordei antes das 10 com fome
if acordei_antes_10 and fome:
    print('Hora de fazer o café da manhã !!!')
else:
    print('Hora de fazer o almoço !!! Vagabundo !!!!')

#acordei antes das 10 com fome mas não é hora do café OBS: no lugar do and pode usar o OR
if acordei_antes_10 and fome2:
    print('Hora de fazer o café da manhã !!!')
elif acordei_antes_10 and not (fome2) :
    print('Hora de correr!! CAVALO !!!!!')
else:
    print('Hora de fazer o almoço !!! Vagabundo !!!!')
