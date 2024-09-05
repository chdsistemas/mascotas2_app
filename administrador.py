# Clase administrador

class Administrador:
    def __init__(self,  nombre = None, profesion=None):
        self.nombre = nombre
        self.profesion = profesion

    def imprimir_datos(self):
        if self.nombre == None:
            print('Nombre no inicializado')
        if .self.profesion == None:
            print('Profesión no se ha inicializado')
        else:
            print(f'Mis datos son: {self.nombre} -- {self.profesion}')
        

ad1 = Administrador()
ad1.nombre = 'Saul'
ad1.profesion = 'Palomar'
ad1.imprimir_datos()






