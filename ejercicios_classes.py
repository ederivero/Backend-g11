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

print(operaciones.dividir())