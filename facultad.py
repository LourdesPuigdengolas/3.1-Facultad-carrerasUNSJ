
class Facultad:
    __codigo:int
    __nombre:str
    __direc:str
    __localidad:str
    __telefono:str
    __listaCarreras: list  #composición al tener la otra lista dentro de esta
    
    def __init__(self, codigo, nombre,direc,localidad,telefono):
        self.__codigo= codigo
        self. __nombre= nombre
        self.__direc=direc
        self.__localidad= localidad
        self.__telefono=telefono
        self.__listaCarreras = []

    def agregarCarrera(self, carrera):
        self.__carreras.append(carrera)

    def get_codigo(self):
        return self.__codigo
    def get_nombre(self):
        return self.__nombre
    def get_direc(self):
        return self.__direc
    def get_localidad(self):
        return self.__localidad
    def get_telefono(self):
        return delf.__telefono
        
    def __str__(self):
        return f'{self.__nombref}'

    
