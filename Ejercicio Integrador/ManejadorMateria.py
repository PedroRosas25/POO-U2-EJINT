import  csv
from ClaseMateria import Materia
from ManejadorAlumno import ManeAlumno
class ManeMater:
    __materias = []
    def __init__(self):
        self.__materias = []
    def __str__(self):
            materias_str = "\n".join([str(materia) for materia in self.__materias])
            return "%s" % materias_str
    def cargarMaterias(self):
        archivo = open("materiasAprobadas.csv")
        r = csv.reader(archivo,delimiter=";")
        bandera = True
        for fila in r:
            if bandera:
                bandera = not bandera
            else:
                dni = fila[0]
                nm = fila[1]
                fecha = fila[2]
                nota = fila[3]
                apro = fila[4]
                materia = Materia(dni, nm, fecha, nota, apro)
                self.__materias.append(materia)
    def tamanio(self):
        return len(self.__materias)
    def buscaralum(self, dni):
        c = 0
        s = 0
        for i in range(len(self.__materias)):
            if (self.__materias[i].getDNI() == dni):  
                c +=  self.__materias[i].getNota() 
                s+=1
        return (c/s)
    def doc(self,i):
        return self.__materias[i].getDNI()
    def unaNota(self,indice):
        return self.__materias[indice].getNota()
    def unaFecha(self,indice):
        return self.__materias[indice].getFecha()
    def unaMateria(self,indice):
        return self.__materias[indice].getNombreMat()
    def unaAprob(self, indice):
        return self.__materias[indice].getAprobacion()
    def promA(self,dni):
        c = 0
        s = 0
        for i in range(len(self.__materias)):
            if int(self.__materias[i].getDNI()) == int(dni):
                s += self.__materias[i].getNota()
                c += 1
        return float(s/c)
    def promB(self,dni):
        c = 0
        s = 0
        for i in range(len(self.__materias)):
            if int(self.__materias[i].getDNI()) == int(dni) and int(self.__materias[i].getNota())>=4:
                s += self.__materias[i].getNota()
                c += 1
        return float(s/c)
                    

           
                    
                

