#1 Definir una variable edad y asignarle un valor entero
edad = 21
print(edad)
edad_cadena = str(edad)
print(edad_cadena)
print(type(edad_cadena))
edad_en_2035 = (2035-2023) + edad
print(edad_en_2035)

#2 Cambiar de orden y sacar cadena por pantalla
cadena = "azebaC ellehciM, 01"
cadena_cambiada = cadena[::-1] #Empieza a leerlos desde el último valor(-1)
print(cadena_cambiada)
print(cadena_cambiada[4::], "ha sacado un", cadena_cambiada[:2])

#3 Determina si una cadena tiene una longitud mayor o igual a 3 y menor o igual a 12 (T/F)
cadena2 = input('Escribe un texto: ')
print('¿La longitud de su texto es mayor o igual que 3 pero menor o igual que 12?', len(cadena2) >=3 and len(cadena2) <=12)

#4 Programa que lee 2 números por teclado y determine x aspectos
n1 = float(input("ingresa el primer número: "))
n2 = float(input("ingresa el segundo número: "))
print("¿Los números son iguales? Respuesta:", n1 == n2)
print("¿Los números son diferentes? Respuesta:", n1 != n2)
print("¿El primero es mayor que el segundo? Respuesta:", n1 > n2)
print("¿El segundo es mayor o igual que el primero? Respuesta:", n1 <= n2)