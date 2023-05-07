from ClaseAlumno import Alumno
from ManejadorAlumno import ManeAlumno
from ClaseMateria import Materia
from ManejadorMateria import ManeMater
class Menu:
    __opciones = 0
    def __init__(self):
        __opciones = 0
    def ops(self,alumnos, materias):
        while self.__opciones != 4:
            print("Opcion 1: Informar promedio de alumno deseado\nOpcion 2: Aprobrados con promocion de materia deseada\nOpcion 3: Obtener listado de alumnos\nOpcion 4: Salir.")
            self.__opciones = int(input("Ingrese opcion deseada. "))
            if self.__opciones == 1:
                dni = int(input("Ingrese dni a buscar "))
                if materias.promA(dni) != 0:
                    print('Promedio del alumno con aplazo {:.2f}'.format(materias.promA(dni)))
                if materias.promB(dni) != 0:
                    print('Promedio del alumno sin aplazos {:.2f}'.format(materias.promB(dni)))
            elif self.__opciones == 2:
                materia = str(input('Ingrese materia a mostrar alumnos que promocionaron. '))
                alumnos.buscaralum(materia, materias)
                pass
            elif self.__opciones == 3:
                print('LISTA ORDENADA:')
                print("{:<15} {:<10} {:<15} {:<5} {:<8}".format("DNI:", "Nombre:", "Apellido", "Carrera", "Año"))
                listaOrdenada = alumnos.ordenar()
                alumnos.mostrar(listaOrdenada)
                
