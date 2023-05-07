import numpy as np
import csv
from ClaseAlumno import Alumno
class ManeAlumno:
    __alumnos = []
    def __init__(self):
        self.__len = 0
        self.__incremento = 4
        self.__cant = 0
        self.__alumnos = np.empty(self.__len, dtype=Alumno)
    def __str__(self):
        alumnos_str = "\n".join([str(alumno) for alumno in self.__alumnos[:self.__cant]])
        return "\n %s" % alumnos_str
    def cargarArreglo(self, alumn):
         if self.__len == self.__cant:
            self.__len += self.__incremento
            self.__alumnos.resize(self.__len)
         self.__alumnos[self.__cant]= alumn
         self.__cant+=1
    def abrirAlumnos(self):
        archivo = open("alumnos.csv")
        reader = csv.reader(archivo,delimiter=";")
        bandera = True
        for fila in reader:
            if bandera:
                    bandera= not bandera
            else:
                    dni=fila[0]
                    ape=fila[1]
                    nomb=fila[2]
                    carre=fila[3]
                    año=fila[4]
                    alumno=Alumno(dni,ape,nomb,carre, año)
                    self.cargarArreglo(alumno)
    def buscaralum(self, materia, lista):
         print('Alumnos que aprobaron por promocion la materia ingresada:')
         print('DNI\t\tNombre y Apellido\tFecha\t\tNota\t\tAnio')
         for i in range(lista.tamanio()):
              for j in range(self.__len):
                   if materia == lista.unaMateria(i) and self.__alumnos[j].getDNI() == lista.doc(i) and lista.unaNota(i) >= 7 and lista.unaAprob(i) == 'P':
                        print('{}\t{} {}\t\t{}\t{}\t\t{}'.format(self.__alumnos[j].getDNI(),self.__alumnos[j].getNombre(),self.__alumnos[j].getApellido(),lista.unaFecha(i),lista.unaNota(i),self.__alumnos[j].getAño()))
    def ordenar(self):
         alumnosordenados = sorted(self.__alumnos)
         return alumnosordenados
    def mostrar(self, listOrd):
         for i in range(self.__len):
              print(listOrd[i])