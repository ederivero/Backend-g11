class Producto:
    def __init__(self, nombre, precio, cantidad, fecha_vencimiento):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.fecha_vencimiento = fecha_vencimiento
        # __atributo > privado > significa que no se puede acceder a esta informacion desde fuera de la clase
        self.__ganancia = 0.3
        # _atributo > protegido > en python se suele utilizar la configuracion de atributos y metodos protegidos para cuestiones de herencia . Puede ser accedido desde dentro y fuera de la clase pero cuando se esta heredando la clase no se puede acceder a este elemento
        self._otro= False

    def __prueba(self):
        self.__ganancia
        print(self.__ganancia)
    
    def mostrar_valor_venta(self):
        return {
            'valor_venta': (self.precio * self.__ganancia ) + self.precio
        }



pitahaya = Producto('pitahaya', 4.50, 100, '2023-02-22')
print(pitahaya.nombre)
# print(pitahaya.__ganancia)
# pitahaya.__prueba()
print(pitahaya.mostrar_valor_venta())