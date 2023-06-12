nombre = input('Como te llamas? ')
print('Hola ' + nombre)

edad = int(input('Cuantos años tienes? '))
esMayorDeEdad = edad >= 18

respuestaHijoDelDueño = input('Eres hijo del dueño? ')
esHijoDelDueño = respuestaHijoDelDueño == 'si'
puedePasar = esMayorDeEdad or esHijoDelDueño

if puedePasar:
  print('Puedes pasar')
else:
  print('No puedes pasar')

#OR (AQUI NO ES ELSE IF, ES ELIF)

if puedePasar:
  print('Puedes pasar')
elif not esMayorDeEdad and not esHijoDelDueño:
  print('No puedes pasar')
