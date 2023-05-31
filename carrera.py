
class Carrera:
    __codigo:int
    __nombre:str
    __fechaIni:str
    __duracion:str
    __titulo:str

    def init(self, codigo, nombre,__fechaIni,titulo,duracion):
        self.__codigo= codigo
        self.__nombre= nombre
        self.__duracion= duracion
        self.__titulo= titulo

    def get_codigo(self):
        return self.__codigo
    def get_nombre(self):
        return self.__nombre
    def get_duracion(self):
        return self.__duracion
    def get_titulo(self):
        return self.__titulo
    def get_fechaIni(self):
        return self.__fechaIni
        
    def __str__(self):
        return f'{self.__nombrec} {self.__duracion}'