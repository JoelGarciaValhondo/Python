
class Cuadrado:
  def __init__(self, a, b) -> None:
      self.ancho = a 
      self.alto = b

  def calcularArea(self):
      area = self.ancho * self.alto
      return area


figura = Cuadrado(10, 12)
print(figura.calcularArea())

#SEGUNDO EJEMPLO

#CLASE BASE PARA EMPLEADO Y CLIENTE
class Persona:
  def __init__(self, nombre, apellido, dni, telefono) -> None:
      self.nombre = nombre
      self.apellido = apellido
      self.dni = dni
      self.telefono = telefono

class Empleado(Persona):
  def __init__(self, nombre, apellido, dni, telefono, salario) -> None:
      super().__init__(nombre, apellido, dni, telefono)
      self.salario = salario

  #NECESITA SER __STR__ SIEMPRE
  def __str__(self):
    datosEmpleado = self.nombre + " " + self.apellido + " "+ self.dni
    return datosEmpleado

class Cliente(Persona):
  def __init__(self, nombre, apellido, dni, telefono, categoria) -> None:
      super().__init__(nombre, apellido, dni, telefono)
      self.categoria = categoria

  #NECESITA SER __STR__ SIEMPRE
  def __str__(self):
    datosCliente = self.nombre + " " + self.apellido + " " + self.dni
    return datosCliente

empleados = []

clientes = []


def cargar():
  ingreso = "si"
  while ingreso.lower == 'si':
    respuesta = input('¿Vas a agregar a un empleado?')
    nombre = input('ingrese el nombre: ')
    apellido = input('ingrese el apellido: ')
    dni = input('ingrese el dni: ')
    telefono = input('ingrese el telefono: ')
    if respuesta == 'si':
      sueldo = input('ingrese el sueldo: ')
      emp = Empleado(nombre, apellido, dni, telefono, int(sueldo)) 
      empleados.append(emp)
    else:
      categoria = input("ingrese la categoria")
      cli = Cliente(nombre, apellido, dni, telefono, categoria)
      clientes.append(cli)
    ingreso = input("¿Quieres seguir ingresando personas?")

cargar()
    
  

