from pprint import pprint
# Crear una Classe Operaciones con sus respectivos métodos
# (sumar, restar, multiplicar y dividir). Esta clase recibirá dos números.

class OperacionesMatematicas:
    
    def __init__(self, valor_1, valor_2):
        self.a = valor_1
        self.b = valor_2

    def sumar(self):
        return self.a + self.b
    
    def restar(self):
        return self.a - self.b
    
    def multiplicar(self):
        return self.a * self.b
    
    def dividir(self):
        return self.__redondear(self.a / self.b)
    
    def __redondear(self, numero):
        return round(numero, 2)

operaciones = OperacionesMatematicas(5, 3)

# print(operaciones.dividir())

# Crear una clase Usuario que recibar los datos de un usuario
# (nombre, edad, dni, estatura, estado civil) y convertir estos datos en un diccionario

class Usuario:
    def __init__(self, nombre, edad, dni, estatura, estado_civil) -> None:
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
        self.estatura = estatura
        self.estado_civil = estado_civil
      
    def convertirDiccionario(self):
        return {
            'nombre': self.nombre,
            'edad': self.edad,
            'dni': self.dni,
            'estatura': self.estatura,
            'estado_civil': self.estado_civil
        }
    
usuario = Usuario('Paolo', 25, 77337722, 1.80, 'soltero')

pprint(usuario.convertirDiccionario())