from ClaseAlumno import Alumno
from ManejadorAlumno import ManeAlumno
from ClaseMateria import Materia
from ManejadorMateria import ManeMater
from ClaseMenu import Menu
if __name__ == "__main__":
    c = ManeAlumno()
    c.abrirAlumnos()
    m = ManeMater()
    m.cargarMaterias()
    menux = Menu()
    menux.ops(c,m)