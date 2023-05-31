from facultad import Facultad
from carrera import Carrera
import csv

class ManejadorFacultades:
    #cargar los datos de ManejaFacultades.csv en una lista de objetos de tipo Facultad..
    __listaFacultades: list

    def __init__(self):
        self.__listaFacultades = []

    def get_facultad(self,i):
        return self.__listaFacultades[i]

    def agregar_facultad(self, unaFacultad):
        self.__listaFacultades.append(unaFacultad) 

    def cargarFacultades(self):
        with open("Facultades.csv") as archivo:
                reader = csv.reader(archivo, delimiter=',')
                indice=0
                for fila in reader:
                    if int(fila) == indice:
                        unaCarrera= Carrera(int(fila[1]),fila[2],fila[3],fila[4], fila[5])
                        self.__listaFacultades[indice-1].agregar_carrera(unaCarrera)
                    else:
                        unaFacultad = Facultad(int(fila[0]),fila[1],fila[2],fila[3],fila[4])
                        self.__listaFacultades.append(unaFacultad)
                        indice+=1

    def buscarFacultades(self, codigo):
        i=0
        bandera = False
        retorno = -1
        while not bandera and i<len(self.__facultades):
            if codigo == self.__listaFacultades[i].get_codigof():
                bandera = True
                retorno = i
            i+=1
        return retorno
    
    def buscarCarreras(self, nom):
        bandera = False
        i=0
        while not bandera and i<len(self.__listaFacultades):
            j=0
            carreras = self.__listaFacultades[i].get_carreras()
            while not bandera and j<len(carreras):
                if carreras[j].get_nombrec() == nombre_carrera:
                    bandera = True
                j+=1
            i+=1
        if not bandera:
            print('No se encontro la carrera')
        else:
            print(f'Codigo de Carrera: {self.__listaFacultades[i-1].get_codigof()}.{carreras[j-1].get_codigoc()}')
            print(f'{self.__listaFacultades[i-1].get_nombref()} {self.__listaFacultades[i-1].get_localidad()}')


    def mostrarFacultades(self,codigo):
        i = self.buscarFacultades(codigo)
        if i != -1:
            facultadBuscada = self.get_facultad(i)
            print(facultadBuscada)
            for carrera in facultadBuscada.get_carreras():
                print(carrera)
        else:
            print('No se encontro Facultad con ese codigo')
            
    def mostrarCarreras(self,nombre_carrera):
       self.buscarCarrera(nombre_carrera)
