#numero = int(input('Ingrese un numero '))

#if numero % 2 == 0:
  #print('El numero es par')
#else:
  #print('El numero es impar')

#hasta aqui facil

#calcular IMC:
#IMC = Peso/(Altura x Altura)  
# < 19 delgado
# entre 20 y 25 normal
# entre 26 y 30 sobrepeso
# > 30 obesidad

peso = int(input('Ingrese su peso en kg '))
altura = float(input('Ingrese su altura en metros '))

#Esto es una funcion
def calcularIMC(peso, altura):
  imc = peso / (altura * altura)
  return imc

imc = calcularIMC(peso, altura)
if imc < 19:
  print('Estado de delgadez')
if imc >= 19 and imc < 25:
  print('Peso normal')
if imc >= 26 and imc < 30:
  print('Estado de sobrepeso')
if imc >= 30:
  print('Estado de obesidad')
