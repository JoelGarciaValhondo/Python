#Formateos
frase = '{} es el primer valor y {} es el segundo'.format(1,2)
print(frase)

#otra forma de formateo
frase2 = 'En este caso alteramos el orden y el {1} apartece primero, luego el {0}'.format('uno', 'dos')
print(frase2)

#otra funcion del formateo
nombre = 'la cartuja de parma'
x = .7
print(f'el valor de {nombre} es', x)
#la f coloca la variable nombre dentro, sin él nos coloca {nombre} literalmente.

#MÉTODOS

#1
print(f'el valor de {nombre.title()} es', x, 'dólares por el papel')

#2
diccionario = {'uno':x, 'dos':x.__add__(10)}
print(diccionario)

#3
print(f'{nombre.title()} cuesta {diccionario["uno"]} pesos y el otro libro {diccionario["dos"]} pesos.')