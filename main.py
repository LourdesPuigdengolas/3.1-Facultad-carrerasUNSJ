from facultad import Facultad
from carrera import Carrera
from manejador import ManejadorFacultades

if __name__=='__main__':

    facultades = ManejadorFacultades()
    facultades.cargarFacultades()
    print('----MENU---')
    print('1. Mostrar nombre de la facultad, nombre y duracion de las carreras.')
    print('2. Dado el nombre de una carrera, mostrar código, nombre y localidad de la facultad donde esta se dicta.')
    print(f"[0]. Salir")
       
    opcion= int(input("Ingrese el numero de opción que desea: "))
    while opcion != 0:
            if opcion == 1:
                codigo= int(input('Ingrese el codigo de la facultad:'))  
                mostrarFacultades(facultades, codigo) 
            elif opcion == 2:
                nom= str(input('Ingrese el nombre de la carrera: '))
                mostrarCarrera(facultades, nom)
                
            opcion= int(input("Ingrese el numero de opción que desea: "))   
    


