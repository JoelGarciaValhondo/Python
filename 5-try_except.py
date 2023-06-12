try:
  print(100/0)
except ZeroDivisionError as e:
  print('caught ZeroDivisionError: ' + str(e))

#OR // PROBAR AMBOS (EL DE EXPCEPTION CREO QUE ES MÁS ESPECÍFICO)

try:
  print(100/0)
except ZeroDivisionError as e:
  print('caught ZeroDivisionError: ' + str(e))
except Exception as e:
  print('caught Exception: ' + str(e))  