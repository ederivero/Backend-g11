class Producto:
    def __init__(self, nombre, precio, cantidad, fecha_vencimiento):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.fecha_vencimiento = fecha_vencimiento
        # __atributo > privado > significa que no se puede acceder a esta informacion desde fuera de la clase
        self.__ganancia = 0.3

    def __prueba(self):
        self.__ganancia
        print(self.__ganancia)



pitahaya = Producto('pitahaya', 4.50, 100, '2023-02-22')
print(pitahaya.nombre)
# print(pitahaya.__ganancia)
pitahaya.__prueba()