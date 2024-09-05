#Crear una clase Producto

class Producto:
    def __init__(self, codigo=None, nombre=None, precio=None, stock=None):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def imprimir_datos(self):
        print(self.codigo)
        print(self.nombre)
        print(self.precio)
        print(self.stock)

producto1 = Producto()
