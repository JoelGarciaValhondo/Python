
def encriptar(texto):
  textoFinal = ''
  for letra in texto:
    textoFinal += letra + 'x'
  return textoFinal

def desencriptar(texto):
  textoFinal = ''
  contador = 0
  for letra in texto:
    if contador % 2 == 0:
      textoFinal += letra 
    contador += 1
  return textoFinal

encriptar("Prueba de texto")
desencriptar("Pxrxuxexbxax xdxex xtxexxxtxox")


def encriptarArchivo():
  archivo1 = open('textoEncriptar.txt', 'r')
  texto = archivo1.read()
  textoEncriptado = encriptar(texto)
  archivo1.close()

  archivo2 = open('textoEncriptado.txt', 'a')
  archivo2.write(textoEncriptado)
  archivo2.close()

encriptarArchivo()