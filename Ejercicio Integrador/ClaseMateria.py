import datetime
class Materia:
    __DNI = ""
    __nm = ""
    __fecha = datetime
    __nota = 0
    __aprob = ''
    def __init__(self, DNI, nm, fecha, nota, aprobacion):
        self.__DNI = DNI
        self.__nm = nm
        self.__fecha = fecha
        self.__nota = nota
        self.__aprob = aprobacion
    def __str__(self):
        return '{} {} {} {} {}'.format(self.__DNI, self.__nm,self.__fecha, self.__nota, self.__aprob)
    def getDNI(self):
        return (self.__DNI)
    def getNombreMat(self):
        return self.__nm
    def getFecha(self):
        return self.__fecha
    def getNota(self):
        return int(self.__nota)
    def getAprobacion(self):
        return self.__aprob
    
    
