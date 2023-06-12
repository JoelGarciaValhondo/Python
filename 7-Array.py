array = {'platano', 'melon', 'sandia'}

array.add("kiwi")
array.remove("melon")


for fruta in array:
  print("Las frutas son: " + fruta) 

array.clear()
print("Ahora ya no hay frutas")

#MÁS EJEMPLOS

#1
diccionario = {
  "Programar": "Programar es transformar el cafe en codigo",
  "POO": "Programación orientada a objetos",
  "MVC": "Modelo Vista Controlador"
}

print(diccionario["POO"])

#2
numeros = {
  "0": "Cero",
  "1": "Uno",
  "2": "Dos"
}

texto = input("Ingrese un numero: ")

textoFinal = ""
for letra in texto:
  textoFinal += numeros[letra]

print(textoFinal) 