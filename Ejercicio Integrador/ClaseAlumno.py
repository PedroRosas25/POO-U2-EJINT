class Alumno:
    __DNI= ""
    __ap = ""
    __nomb = ""
    __carr = ""
    __año  = 0
    def __init__(self, dni='', ap='', nomb='', carr='', año=0):
        self.__DNI = dni
        self.__ap = ap
        self.__nomb = nomb
        self.__carr = carr
        self.__año = año
    def __str__(self):
        return "{:<15} {:<10} {:<15} {:<8} {:<5}" .format(self.__DNI, self.__nomb, self.__ap, self.__carr, self.__año)
    def getDNI(self):
        return self.__DNI
    def getApellido(self):
        return self.__ap
    def getNombre(self):
        return str(self.__nomb)
    def getCarrera(self):
        return self.__carr
    def getAño(self):
        return self.__año
    def __lt__(self, otro):
        return (self.__año,self.__ap,self.__nomb)<(otro.__año,otro.__ap,otro.__nomb)
            
